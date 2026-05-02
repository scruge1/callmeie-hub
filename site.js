/* callmeie.ie — minimal motion script.
   Single concern: trigger Fraunces variable-font-axis kinetic load on the hero
   headline once fonts are ready. Pure CSS transition does the animation; this
   script just adds .is-loaded after first paint.

   prefers-reduced-motion: short-circuits before the class is added.
*/

(function () {
  'use strict';

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.headline').forEach(function (el) {
      el.style.fontVariationSettings = "'wght' 500, 'opsz' 144";
    });
    return;
  }

  function reveal() {
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        document.querySelectorAll('.headline').forEach(function (el) {
          el.classList.add('is-loaded');
        });
      });
    });
  }

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(reveal);
  } else {
    window.addEventListener('load', reveal);
  }
})();
