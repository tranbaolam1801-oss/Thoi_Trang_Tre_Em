function formatTime(seconds) {
  const h = Math.floor(seconds / 3600).toString().padStart(2, "0");
  const m = Math.floor((seconds % 3600) / 60).toString().padStart(2, "0");
  const s = Math.floor(seconds % 60).toString().padStart(2, "0");
  return `${h}:${m}:${s}`;
}

function initFlashSaleCountdown() {
  const countdownEl = document.getElementById("countdown");
  if (!countdownEl) return;

  let remaining = parseInt(countdownEl.dataset.remaining ?? "0", 10);
  if (Number.isNaN(remaining) || remaining < 0) {
    countdownEl.textContent = "00:00:00";
    return;
  }

  const update = () => {
    countdownEl.textContent = formatTime(remaining);
    if (remaining <= 0) {
      clearInterval(timer);
      countdownEl.textContent = "00:00:00";
      return;
    }
    remaining -= 1;
  };

  update();
  const timer = setInterval(update, 1000);
}

function getCartCount() {
  const raw = localStorage.getItem("cart_count");
  const count = parseInt(raw, 10);
  return Number.isNaN(count) ? 0 : count;
}

function setCartCount(count) {
  const el = document.getElementById("cart-count");
  if (!el) return;
  el.textContent = String(count);
  localStorage.setItem("cart_count", String(count));
}

function showToast(message) {
  const toast = document.getElementById("toast");
  if (!toast) return;
  toast.textContent = message;
  toast.classList.remove("hidden");
  toast.classList.add("opacity-0");

  requestAnimationFrame(() => {
    toast.classList.remove("opacity-0");
    toast.classList.add("opacity-100");
  });

  clearTimeout(window.__toastTimeout);
  window.__toastTimeout = setTimeout(() => {
    toast.classList.add("opacity-0");
    toast.addEventListener(
      "transitionend",
      () => toast.classList.add("hidden"),
      { once: true }
    );
  }, 2500);
}

function addToCart(productId, productName) {
  const current = getCartCount();
  setCartCount(current + 1);
  showToast(`Đã thêm "${productName}" vào giỏ hàng`);
}

function initCartFromStorage() {
  setCartCount(getCartCount());
}

document.addEventListener("DOMContentLoaded", () => {
  initFlashSaleCountdown();
  initCartFromStorage();
});
