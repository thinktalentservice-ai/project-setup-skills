(() => {
  // ── Toast ────────────────────────────────────────
  function showToast(msg) {
    const t = document.getElementById('toast');
    if (!t) return;
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(t._timer);
    t._timer = setTimeout(() => t.classList.remove('show'), 2000);
  }

  // ── Copy to clipboard ─────────────────────────────
  function copyText(text, btn) {
    navigator.clipboard.writeText(text).then(() => {
      const originalNodes = Array.from(btn.childNodes).map(n => n.cloneNode(true));
      btn.replaceChildren();
      const icon = document.createElement('i');
      icon.className = 'bi bi-check2';
      btn.appendChild(icon);
      btn.appendChild(document.createTextNode(' Copied!'));
      btn.classList.add('copy-success');
      showToast('Copied');
      setTimeout(() => {
        btn.replaceChildren(...originalNodes);
        btn.classList.remove('copy-success');
      }, 1800);
    });
  }

  // ── Code block copy buttons ───────────────────────
  document.querySelectorAll('[data-copy-block]').forEach(btn => {
    btn.addEventListener('click', () => {
      const wrap = btn.closest('[data-code-wrap]');
      const pre = wrap ? wrap.querySelector('pre') : null;
      if (pre) copyText(pre.innerText.trim(), btn);
    });
  });

  // ── Inline copytext elements ──────────────────────
  document.querySelectorAll('[data-copytext]').forEach(el => {
    el.style.cursor = 'pointer';
    el.title = 'Click to copy';
    el.addEventListener('click', () => copyText(el.dataset.copytext, el));
  });

  // ── Tabs ──────────────────────────────────────────
  document.querySelectorAll('[data-tab-group]').forEach(group => {
    const id = group.dataset.tabGroup;
    const btns   = document.querySelectorAll(`[data-tab="${id}"]`);
    const panels = document.querySelectorAll(`[data-tab-panel="${id}"]`);

    function activate(target) {
      btns.forEach(b => {
        const isActive = b.dataset.tabTarget === target;
        b.classList.toggle('text-green-400',   isActive);
        b.classList.toggle('border-green-400', isActive);
        b.classList.toggle('text-slate-400',  !isActive);
        b.classList.toggle('border-transparent', !isActive);
      });
      panels.forEach(p => {
        p.classList.toggle('hidden', p.dataset.tabPanelId !== target);
      });
    }

    btns.forEach(b => b.addEventListener('click', () => activate(b.dataset.tabTarget)));
    if (btns[0]) activate(btns[0].dataset.tabTarget);
  });

  // ── Scroll reveal ─────────────────────────────────
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.08 });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  // ── Sticky nav shadow ─────────────────────────────
  const nav = document.querySelector('nav');
  window.addEventListener('scroll', () => {
    nav?.classList.toggle('shadow-lg', window.scrollY > 8);
  }, { passive: true });
})();
