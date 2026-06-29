// This is a single-line comment
const swiper = new Swiper('.mySwiper', {
  loop:true,

  autoplay:{
    delay:3000,
    disableOnInteraction:false,
  },

  pagination:{
    el:'.swiper-pagination',
    clickable:true,
  },
});

// This is a single-line comment
  (function() {
    const isMobile = /Android|iPhone|iPad|iPod/i.test(navigator.userAgent);
    
    if (isMobile) {
      let meta = document.querySelector('meta[name="viewport"]');
      if (!meta) {
        meta = document.createElement('meta');
        meta.name = "viewport";
        document.head.appendChild(meta);
      }
      
      meta.content = "width=1200, initial-scale=0.3, user-scalable=no";
      
      document.body.style.minWidth = "120px";
    }
  })();
  
  