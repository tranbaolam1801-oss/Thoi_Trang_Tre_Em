function showToast(message) {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = message;
  toast.classList.remove('hidden');
  toast.classList.add('opacity-0');

  requestAnimationFrame(() => {
    toast.classList.remove('opacity-0');
    toast.classList.add('opacity-100');
  });

  clearTimeout(window.__toastTimeout);
  window.__toastTimeout = setTimeout(() => {
    toast.classList.add('opacity-0');
    toast.addEventListener(
      'transitionend',
      () => toast.classList.add('hidden'),
      { once: true }
    );
  }, 2500);
}

function initCartCount() {
  const el = document.getElementById('cart-count');
  if (!el) return;
  // Cart count is rendered server-side via context processor
}

document.addEventListener('DOMContentLoaded', () => {
  initCartCount();
});
