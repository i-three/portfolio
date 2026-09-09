/**
 * AN. design & cording — Portfolio
 * Vanilla JS only: mobile nav, scroll-reveal, contact form handling.
 */

(() => {
  'use strict';

  /* ---------------- Mobile nav ---------------- */
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');

  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const isOpen = links.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(isOpen));
      toggle.querySelector('.material-symbols').textContent = isOpen ? 'close' : 'menu';
    });

    links.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        links.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.querySelector('.material-symbols').textContent = 'menu';
      });
    });
  }

  /* ---------------- Scroll reveal ---------------- */
  const revealEls = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window && revealEls.length) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
    );

    revealEls.forEach((el) => observer.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('is-visible'));
  }

  /* ---------------- Contact form ---------------- */
  // Set this to your form backend endpoint (e.g. a Formspree / Getform URL)
  // to receive submissions without a server. Until it's set, the form falls
  // back to opening the visitor's email client with the message pre-filled.
  const FORM_ENDPOINT = ''; // e.g. 'https://formspree.io/f/xxxxxxx'
  const CONTACT_EMAIL = 'aiko.nakamura.pj@gmail.com';

  const form = document.querySelector('#contact-form');
  const status = document.querySelector('#form-status');

  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const name = data.get('name');
      const email = data.get('email');
      const message = data.get('message');

      if (!FORM_ENDPOINT) {
        const subject = encodeURIComponent(`ポートフォリオサイトからのお問合せ（${name}様）`);
        const body = encodeURIComponent(`お名前: ${name}\nメールアドレス: ${email}\n\n${message}`);
        window.location.href = `mailto:${CONTACT_EMAIL}?subject=${subject}&body=${body}`;
        showStatus('success', 'メールソフトを開きました。送信を完了してください。');
        return;
      }

      try {
        const res = await fetch(FORM_ENDPOINT, {
          method: 'POST',
          headers: { Accept: 'application/json' },
          body: data,
        });

        if (res.ok) {
          form.reset();
          showStatus('success', 'お問合せありがとうございます。内容を送信しました。');
        } else {
          showStatus('error', '送信に失敗しました。時間をおいて再度お試しください。');
        }
      } catch (err) {
        showStatus('error', '送信に失敗しました。通信環境をご確認のうえ再度お試しください。');
      }
    });
  }

  function showStatus(type, message) {
    if (!status) return;
    status.textContent = message;
    status.className = `form-status is-${type}`;
  }
})();
