/* One native scroll pass: authored scene layers move with the page, never pinned. */
(() => {
  const scene = document.querySelector('.studio-hero');
  const preference = matchMedia('(prefers-reduced-motion: reduce)');
  if (!scene) return;
  let pending = false;
  const paint = () => {
    pending = false;
    const box = scene.getBoundingClientRect();
    const progress = preference.matches ? 0 : Math.max(0, Math.min(1, -box.top / box.height));
    scene.style.setProperty('--scene-depth', String(progress));
  };
  const schedule = () => {
    if (pending) return;
    pending = true;
    requestAnimationFrame(paint);
  };
  addEventListener('scroll', schedule, { passive: true });
  addEventListener('resize', schedule, { passive: true });
  preference.addEventListener('change', schedule);
  paint();
})();
