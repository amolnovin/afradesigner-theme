/* =====================================================
   افرا حسین‌زاده — اسکریپت اصلی قالب پرسونال برندینگ
   ===================================================== */
(function () {
  "use strict";

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const esc = (str) =>
    String(str ?? "").replace(/[&<>"']/g, (m) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[m]));
  const fa = (n) => Number(n).toLocaleString("fa-IR");
  const reducedMotion = () => matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- تم (تاریک پیش‌فرض برندینگ / روشن کاغذی) ---------- */
  const root = document.documentElement;
  const savedTheme = localStorage.getItem("afra-theme");
  if (!root.dataset.theme || root.dataset.theme === "auto") {
    root.dataset.theme = savedTheme || "dark";
  }
  $$("[data-theme-toggle]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const isDark =
        root.dataset.theme === "dark" ||
        (root.dataset.theme === "auto" && matchMedia("(prefers-color-scheme: dark)").matches);
      root.dataset.theme = isDark ? "light" : "dark";
      localStorage.setItem("afra-theme", root.dataset.theme);
    });
  });

  /* ---------- هدر چسبان + نوار پیشرفت اسکرول ---------- */
  const header = $(".header");
  const toTop = $(".to-top");
  const progressEl = $(".dock-progress");
  const onScroll = () => {
    const y = window.scrollY;
    header && header.classList.toggle("scrolled", y > 10);
    toTop && toTop.classList.toggle("show", y > 520);
    if (progressEl) {
      const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
      progressEl.style.width = Math.min(100, Math.max(0, (y / max) * 100)).toFixed(1) + "%";
    }
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  toTop && toTop.addEventListener("click", () => {
    if ($("#hero")) navigateToSection("hero");
    else window.scrollTo({ top: 0, behavior: "smooth" });
  });

  /* ---------- کشوی منوی همبرگری (گوشه سمت چپ) ---------- */
  const drawer = $(".nav-drawer");
  const drawerBackdrop = $(".drawer-backdrop");
  const openDrawer = () => {
    if (!drawer) return;
    drawer.classList.add("open");
    drawer.setAttribute("aria-hidden", "false");
    drawerBackdrop && drawerBackdrop.classList.add("open");
    document.body.style.overflow = "hidden";
  };
  const closeDrawer = () => {
    if (!drawer) return;
    drawer.classList.remove("open");
    drawer.setAttribute("aria-hidden", "true");
    drawerBackdrop && drawerBackdrop.classList.remove("open");
    document.body.style.overflow = "";
  };
  $$("[data-menu-open]").forEach((b) => b.addEventListener("click", openDrawer));
  $$("[data-menu-close]").forEach((b) => b.addEventListener("click", closeDrawer));
  drawerBackdrop && drawerBackdrop.addEventListener("click", closeDrawer);

  /* ---------- لینک فعال در منوی همبرگری ---------- */
  const currentPage = location.pathname.split("/").pop() || "index.html";
  $$(".nav-drawer nav a").forEach((a) => {
    const href = a.getAttribute("href") || "";
    if (href === currentPage) a.classList.add("active");
    a.addEventListener("click", () => closeDrawer());
  });

  /* ---------- انیمیشن ورود المان‌ها ---------- */
  const io = new IntersectionObserver(
    (entries) =>
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      }),
    { threshold: 0.1 }
  );
  $$(".reveal, .skill").forEach((el) => io.observe(el));

  /* ---------- شمارنده اعداد ---------- */
  const cio = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        const el = e.target,
          target = +el.dataset.count,
          suffix = el.dataset.suffix || "",
          prefix = el.dataset.prefix || "";
        const dur = 1500,
          t0 = performance.now();
        const tick = (t) => {
          const p = Math.min(1, (t - t0) / dur),
            v = Math.round(target * (1 - Math.pow(1 - p, 3)));
          el.textContent = prefix + fa(v) + suffix;
          if (p < 1) requestAnimationFrame(tick);
        };
        requestAnimationFrame(tick);
        cio.unobserve(el);
      });
    },
    { threshold: 0.45 }
  );
  $$("[data-count]").forEach((el) => cio.observe(el));

  /* ---------- Toast ---------- */
  let toastEl = $(".toast");
  if (!toastEl) {
    toastEl = document.createElement("div");
    toastEl.className = "toast";
    toastEl.setAttribute("role", "status");
    document.body.appendChild(toastEl);
  }
  let toastT;
  window.toast = (msg) => {
    toastEl.textContent = msg;
    toastEl.classList.add("show");
    clearTimeout(toastT);
    toastT = setTimeout(() => toastEl.classList.remove("show"), 3200);
  };

  /* =====================================================
     نوار دک پایین صفحه (Bottom Section Dock) + انیمیشن سینمایی
     ===================================================== */
  const dock = $(".section-dock");
  const veil = $(".sec-transition-veil");
  let isProgrammaticScroll = false;
  let scrollTimer = null;
  let animFrame = null;

  const setActiveDock = (secId, pulse = false) => {
    if (!dock) return;
    $$(".dock-item", dock).forEach((item) => {
      const match = item.dataset.sec === secId;
      item.classList.toggle("active", match);
      if (match) {
        if (pulse) {
          item.classList.remove("pulse-click");
          void item.offsetWidth;
          item.classList.add("pulse-click");
        }
        // اسکرول افقی خودکار دک در نمایشگرهای موبایل
        const dockRect = dock.getBoundingClientRect();
        const itemRect = item.getBoundingClientRect();
        if (itemRect.left < dockRect.left + 12 || itemRect.right > dockRect.right - 12) {
          dock.scrollTo({
            left: dock.scrollLeft + (itemRect.left - dockRect.left) - dockRect.width / 2 + itemRect.width / 2,
            behavior: "smooth",
          });
        }
      }
    });
  };

  const smoothScrollToY = (targetY, duration, onDone) => {
    if (animFrame) cancelAnimationFrame(animFrame);
    if (reducedMotion() || duration <= 0) {
      window.scrollTo(0, targetY);
      onDone && onDone();
      return;
    }
    const startY = window.scrollY;
    const diff = targetY - startY;
    const t0 = performance.now();
    const easeInOutQuint = (x) => (x < 0.5 ? 16 * x * x * x * x * x : 1 - Math.pow(-2 * x + 2, 5) / 2);

    const step = (now) => {
      const p = Math.min(1, (now - t0) / duration);
      window.scrollTo(0, startY + diff * easeInOutQuint(p));
      if (p < 1) {
        animFrame = requestAnimationFrame(step);
      } else {
        animFrame = null;
        onDone && onDone();
      }
    };
    animFrame = requestAnimationFrame(step);
  };

  const triggerSpotlight = (sec) => {
    if (!sec || reducedMotion()) return;
    sec.classList.remove("section-spotlight");
    void sec.offsetWidth;
    sec.classList.add("section-spotlight");
    $$(".reveal, .skill", sec).forEach((el) => el.classList.add("in"));
    setTimeout(() => sec.classList.remove("section-spotlight"), 900);
  };

  function navigateToSection(secId) {
    const sec = document.getElementById(secId);
    if (!sec) {
      location.href = "index.html#" + secId;
      return;
    }
    isProgrammaticScroll = true;
    clearTimeout(scrollTimer);
    setActiveDock(secId, true);

    const navH = header ? header.offsetHeight : 76;
    const targetY = secId === "hero" ? 0 : Math.max(0, sec.getBoundingClientRect().top + window.scrollY - navH + 2);
    const distance = Math.abs(targetY - window.scrollY);

    if (veil && !reducedMotion()) {
      veil.classList.add("active");
      setTimeout(() => veil.classList.remove("active"), 520);
    }

    // برای فواصل خیلی دور، جهش نرم دو مرحله‌ای اجرا می‌شود تا حس جابه‌جایی سریع اسلایدی حفظ شود
    if (distance > window.innerHeight * 2.6 && !reducedMotion()) {
      const dir = targetY > window.scrollY ? 1 : -1;
      window.scrollTo(0, Math.max(0, targetY - dir * 180));
      triggerSpotlight(sec);
      smoothScrollToY(targetY, 480, () => {
        history.replaceState(null, "", secId === "hero" ? location.pathname : "#" + secId);
        scrollTimer = setTimeout(() => { isProgrammaticScroll = false; }, 120);
      });
    } else {
      triggerSpotlight(sec);
      smoothScrollToY(targetY, Math.min(760, Math.max(420, distance * 0.45)), () => {
        history.replaceState(null, "", secId === "hero" ? location.pathname : "#" + secId);
        scrollTimer = setTimeout(() => { isProgrammaticScroll = false; }, 120);
      });
    }
  }

  if (dock) {
    $$(".dock-item", dock).forEach((btn) => {
      btn.addEventListener("click", (e) => {
        const secId = btn.dataset.sec;
        if (!secId) return;
        if (document.getElementById(secId)) {
          e.preventDefault();
          navigateToSection(secId);
        }
      });
    });

    // لینک‌های میانبر داخلی سکشن‌ها (در کارت‌های بنتو و هیرو)
    $$("[data-goto-sec]").forEach((el) => {
      el.addEventListener("click", (e) => {
        const secId = el.dataset.gotoSec;
        if (secId && document.getElementById(secId)) {
          e.preventDefault();
          navigateToSection(secId);
        }
      });
    });

    // رصد خودکار سکشن فعال هنگام اسکرول طبیعی در صفحه اصلی
    const homeSections = $$("[data-dock-section]");
    if (homeSections.length) {
      const spy = new IntersectionObserver(
        (entries) => {
          if (isProgrammaticScroll) return;
          const visible = entries
            .filter((en) => en.isIntersecting)
            .sort((a, b) => b.intersectionRatio - a.intersectionRatio);
          if (visible.length) {
            setActiveDock(visible[0].target.id, false);
          }
        },
        { rootMargin: "-28% 0px -45% 0px", threshold: [0.05, 0.25, 0.5] }
      );
      homeSections.forEach((s) => spy.observe(s));

      // اگر با #hash وارد صفحه اصلی شدیم
      if (location.hash) {
        const initialId = location.hash.slice(1);
        if (document.getElementById(initialId)) {
          setTimeout(() => navigateToSection(initialId), 120);
        }
      }
    } else {
      // هایلایت آیکن متناظر در صفحات داخلی
      const pageMap = {
        "services.html": "services",
        "portfolio.html": "portfolio",
        "order.html": "services",
        "consult.html": "consult",
        "about.html": "about",
        "blog.html": "blog",
        "contact.html": "contact",
      };
      if (pageMap[currentPage]) setActiveDock(pageMap[currentPage], false);
    }
  }

  /* =====================================================
     جستجوی هوشمند زنده (آیکن جستجو در گوشه چپ هدر + Ctrl+K)
     ===================================================== */
  const SEARCH_INDEX = [
    { title: "افرا حسین‌زاده — معرفی و برند شخصی", desc: "سکشن اول: معرفی، آمار، رزومه و مسیر همکاری", url: "index.html#hero", sec: "hero", badge: "بخش صفحه اصلی", kw: "خانه معرفی افرا حسین زاده طراح جلد صفحه آرا" },
    { title: "اکوسیستم خدمات طراحی و نشر", desc: "نمای یکپارچه مسیرهای طراحی جلد، صفحه‌آرایی و مشاوره", url: "index.html#hub", sec: "hub", badge: "در یک نگاه", kw: "اکوسیستم هاب خدمات کتاب مجله" },
    { title: "درباره افرا حسین‌زاده و داستان شکل‌گیری", desc: "بیش از ۱۰ سال تجربه همکاری با ناشران و نویسندگان مستقل", url: "about.html", sec: "about", badge: "درباره من", kw: "بیوگرافی رزومه مهارت ایندیزاین تیم افرا" },
    { title: "طراحی جلد کتاب (روی جلد، عطف و پشت جلد)", desc: "۳ اتود اختصاصی + ویرایش نامحدود + خروجی چاپی CMYK", url: "services.html#cover", badge: "خدمت تخصصی", kw: "جلد شومیز گالینگور سخت موکاپ قیمت جلد" },
    { title: "صفحه‌آرایی حرفه‌ای کتاب در Adobe InDesign", desc: "گرید اختصاصی، تایپوگرافی فارسی، پانویس، نمایه و فهرست", url: "services.html#layout", badge: "خدمت تخصصی", kw: "صفحه آرایی چیدمان متن شعر رمان دانشگاهی" },
    { title: "صفحه‌آرایی مجله، نشریه و کاتالوگ", desc: "طراحی ادیتوریال چندستونه، مسترپیج و اینفوگرافیک", url: "services.html#magazine", badge: "خدمت تخصصی", kw: "مجله نشریه کاتالوگ سالنامه ادیتوریال" },
    { title: "تولید کتاب الکترونیک استاندارد (EPUB / PDF)", desc: "مناسب پلتفرم‌های طاقچه، فیدیبو و کتاب‌خوان‌ها", url: "services.html#ebook", badge: "خدمت دیجیتال", kw: "ایبوک کتاب الکترونیک طاقچه فیدیبو epub" },
    { title: "ماشین‌حساب آنلاین برآورد تعرفه و قیمت", desc: "محاسبه آنی هزینه صفحه‌آرایی و طراحی جلد بر اساس تعداد صفحه", url: "services.html#calc-sec", badge: "ابزار محاسبه", kw: "قیمت تعرفه هزینه محاسبه ماشین حساب بسته" },
    { title: "گالری نمونه‌کارهای جلد و صفحه‌آرایی", desc: "مشاهده پروژه‌های انجام‌شده برای نشر چشمه، نگاه، سمت و مروارید", url: "portfolio.html", sec: "portfolio", badge: "نمونه‌کارها", kw: "پورتفولیو گالری نمونه جلد رمان کودک دانشگاهی" },
    { title: "ثبت سفارش آنلاین ۴ مرحله‌ای", desc: "ارسال مشخصات اثر و فایل‌ها همراه با دریافت کد رهگیری", url: "order.html", badge: "ثبت سفارش", kw: "فرم سفارش خرید پروژه فوری" },
    { title: "رزرو جلسه مشاوره رایگان ۲۰ دقیقه‌ای", desc: "انتخاب روز و ساعت در تقویم شمسی (تلفنی، تصویری یا واتساپ)", url: "consult.html", sec: "consult", badge: "مشاوره رایگان", kw: "نوبت وقت مشاوره شابک فیپا چاپ کتاب اول" },
    { title: "دیدگاه ناشران و نویسندگان درباره همکاری با افرا", desc: "تجربه‌های واقعی مشتریان و پاسخ به پرسش‌های متداول", url: "index.html#testimonials", sec: "testimonials", badge: "نظرات مشتریان", kw: "رضایت کامنت دیدگاه سوالات متداول اصلاحات" },
    { title: "مجله تخصصی طراحی کتاب و تایپوگرافی فارسی", desc: "مقالات آموزشی اشتباهات صفحه‌آرایی، انتخاب فونت و قطع کتاب", url: "blog.html", sec: "blog", badge: "مجله و مقالات", kw: "بلاگ آموزش فونت وزیر ایران سنس قطع رقعی وزیری" },
    { title: "راه‌های ارتباط با افرا حسین‌زاده", desc: "تلفن، واتساپ، ایمیل و فرم ارسال پیام مستقیم", url: "contact.html", sec: "contact", badge: "تماس با ما", kw: "شماره تلفن آدرس ایمیل واتساپ تلگرام اینستاگرام" },
  ];

  const searchModal = $("#search-modal");
  const searchInput = $("#search-input");
  const searchResults = $("#search-results");
  let focusIdx = -1;

  const renderSearch = (q = "") => {
    if (!searchResults) return;
    const term = q.trim().toLowerCase();
    const matched = !term
      ? SEARCH_INDEX.slice(0, 8)
      : SEARCH_INDEX.filter((it) => (it.title + " " + it.desc + " " + it.kw + " " + it.badge).toLowerCase().includes(term));
    focusIdx = -1;
    if (!matched.length) {
      searchResults.innerHTML = `<div class="search-empty">نتیجه‌ای برای «<b>${esc(q)}</b>» پیدا نشد. عبارت دیگری را امتحان کنید.</div>`;
      return;
    }
    searchResults.innerHTML = matched
      .map(
        (it) => `
      <a class="search-item" href="${it.url}" ${it.sec ? `data-search-sec="${it.sec}"` : ""}>
        <div>
          <b>${esc(it.title)}</b>
          <small>${esc(it.desc)}</small>
        </div>
        <span class="s-badge">${esc(it.badge)}</span>
      </a>`
      )
      .join("");

    $$(".search-item", searchResults).forEach((a) => {
      a.addEventListener("click", (e) => {
        const secId = a.dataset.searchSec;
        closeSearch();
        if (secId && (currentPage === "index.html" || currentPage === "") && document.getElementById(secId)) {
          e.preventDefault();
          navigateToSection(secId);
        }
      });
    });
  };

  const openSearch = () => {
    if (!searchModal) return;
    searchModal.classList.add("open");
    searchModal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    renderSearch(searchInput ? searchInput.value : "");
    setTimeout(() => searchInput && searchInput.focus(), 60);
  };
  const closeSearch = () => {
    if (!searchModal) return;
    searchModal.classList.remove("open");
    searchModal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  };

  $$("[data-search-open]").forEach((b) => b.addEventListener("click", openSearch));
  $$("[data-search-close]").forEach((b) => b.addEventListener("click", closeSearch));
  searchModal && searchModal.addEventListener("click", (e) => { if (e.target === searchModal) closeSearch(); });
  searchInput && searchInput.addEventListener("input", (e) => renderSearch(e.target.value));
  $$("[data-search-tag]").forEach((t) =>
    t.addEventListener("click", () => {
      if (!searchInput) return;
      searchInput.value = t.dataset.searchTag;
      renderSearch(searchInput.value);
      searchInput.focus();
    })
  );

  /* کلیدهای میانبر سراسری (Ctrl+K / Escape / جهت‌نما در جستجو) */
  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      searchModal && searchModal.classList.contains("open") ? closeSearch() : openSearch();
      return;
    }
    if (e.key === "Escape") {
      if (searchModal && searchModal.classList.contains("open")) closeSearch();
      if (drawer && drawer.classList.contains("open")) closeDrawer();
    }
    if (searchModal && searchModal.classList.contains("open")) {
      const items = $$(".search-item", searchResults);
      if (!items.length) return;
      if (e.key === "ArrowDown") {
        e.preventDefault();
        focusIdx = (focusIdx + 1) % items.length;
        items.forEach((el, i) => el.classList.toggle("focused", i === focusIdx));
        items[focusIdx].scrollIntoView({ block: "nearest" });
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        focusIdx = (focusIdx - 1 + items.length) % items.length;
        items.forEach((el, i) => el.classList.toggle("focused", i === focusIdx));
        items[focusIdx].scrollIntoView({ block: "nearest" });
      } else if (e.key === "Enter" && focusIdx >= 0 && items[focusIdx]) {
        e.preventDefault();
        items[focusIdx].click();
      }
    }
  });

  /* ---------- فیلتر نمونه‌کار + لایت‌باکس ---------- */
  const workGrid = $(".work-grid");
  if (workGrid) {
    const workScope = workGrid.closest("section") || document;
    const works = $$(".work", workGrid);
    $$(".filter-btn", workScope).forEach((btn) => {
      btn.addEventListener("click", () => {
        $$(".filter-btn", workScope).forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        const f = btn.dataset.filter || "all";
        works.forEach((w) => w.classList.toggle("hide", f !== "all" && w.dataset.cat !== f));
      });
    });

    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `
      <button class="lightbox-close" aria-label="بستن"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6 6 18M6 6l12 12"/></svg></button>
      <button class="lightbox-nav prev" aria-label="قبلی"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m9 6 6 6-6 6"/></svg></button>
      <button class="lightbox-nav next" aria-label="بعدی"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 6-6 6 6 6"/></svg></button>
      <div class="lightbox-inner">
        <img alt="">
        <div class="lightbox-body">
          <span class="eyebrow" data-lb="cat"></span>
          <h3 data-lb="title"></h3>
          <p data-lb="desc"></p>
          <div class="meta" data-lb="meta"></div>
          <a href="order.html" data-lb-order class="btn btn-primary" style="margin-top:auto">سفارش پروژه مشابه</a>
        </div>
      </div>`;
    document.body.appendChild(lb);
    let idx = 0;
    const visible = () => works.filter((w) => !w.classList.contains("hide"));
    const show = (i) => {
      const list = visible();
      if (!list.length) return;
      idx = (i + list.length) % list.length;
      const w = list[idx],
        d = w.dataset;
      const lbImg = $("img", lb);
      lbImg.src = $("img", w).src;
      lbImg.alt = d.title || "نمونه‌کار افرا حسین‌زاده";
      $("[data-lb=cat]", lb).textContent = d.catLabel || "";
      $("[data-lb=title]", lb).textContent = d.title || "";
      $("[data-lb=desc]", lb).textContent = d.desc || "";
      $("[data-lb=meta]", lb).innerHTML = (d.meta || "")
        .split("|")
        .filter(Boolean)
        .map((m) => `<span>${esc(m.trim())}</span>`)
        .join("");
      const svcMap = { cover: "cover", layout: "layout", magazine: "magazine", kids: "both", academic: "layout" };
      $("[data-lb-order]", lb).href = "order.html?service=" + (svcMap[d.cat] || "both");
      lb.classList.add("open");
      document.body.style.overflow = "hidden";
    };
    const close = () => {
      lb.classList.remove("open");
      document.body.style.overflow = "";
    };
    works.forEach((w) => w.addEventListener("click", () => show(visible().indexOf(w))));
    $(".lightbox-close", lb).addEventListener("click", close);
    $(".prev", lb).addEventListener("click", () => show(idx - 1));
    $(".next", lb).addEventListener("click", () => show(idx + 1));
    lb.addEventListener("click", (e) => {
      if (e.target === lb) close();
    });
    document.addEventListener("keydown", (e) => {
      if (!lb.classList.contains("open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowRight") show(idx - 1);
      if (e.key === "ArrowLeft") show(idx + 1);
    });
  }

  /* ---------- فیلتر دسته‌بندی مقالات مجله ---------- */
  $$(".blog-grid").forEach((grid) => {
    const scope = grid.closest("section") || document;
    const posts = $$(".post", grid);
    $$(".filter-btn", scope).forEach((btn) => {
      if (!btn.dataset.blogFilter) return;
      btn.addEventListener("click", () => {
        $$(".filter-btn", scope).forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        const f = btn.dataset.blogFilter;
        posts.forEach((p) => p.classList.toggle("hide", f !== "all" && p.dataset.cat !== f));
      });
    });
  });

  /* ---------- انتخابگر نوع جلسه در سکشن مشاوره صفحه اصلی ---------- */
  const reserveCta = $("[data-reserve-cta]");
  $$(".mode-card[data-mode]").forEach((card) => {
    card.addEventListener("click", () => {
      $$(".mode-card[data-mode]").forEach((c) => c.classList.remove("active"));
      card.classList.add("active");
      if (reserveCta) reserveCta.href = "consult.html?mode=" + card.dataset.mode;
    });
  });

  /* ---------- اسلایدر نظرات ---------- */
  const tt = $(".testi-track");
  if (tt) {
    $$("[data-testi]").forEach((b) =>
      b.addEventListener("click", () => {
        const dir = b.dataset.testi === "next" ? -1 : 1;
        tt.scrollBy({ left: dir * 400, behavior: "smooth" });
      })
    );
  }

  /* ---------- اعتبارسنجی فرم عمومی (شامل فیلدهای اختیاری ایمیل/تلفن) ---------- */
  const validateFields = (scope) => {
    let ok = true;
    $$("input, select, textarea", scope).forEach((inp) => {
      const field = inp.closest(".field");
      if (!field) return;
      const val = inp.value ? inp.value.trim() : "";
      let valid = true;
      if (inp.hasAttribute("required")) {
        valid = inp.type === "checkbox" ? inp.checked : val !== "";
      }
      if (valid && val !== "" && inp.type === "email") {
        valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(val);
      }
      if (valid && val !== "" && inp.type === "tel") {
        const norm = val.replace(/[\s-]/g, "").replace(/[۰-۹]/g, (d) => "۰۱۲۳۴۵۶۷۸۹".indexOf(d));
        valid = /^(\+98|0)?9\d{9}$/.test(norm);
      }
      field.classList.toggle("invalid", !valid);
      if (!valid) ok = false;
    });
    $$("[data-required-group]", scope).forEach((g) => {
      const any = $$("input:checked", g).length > 0;
      g.classList.toggle("invalid", !any);
      const err = $(".err", g);
      if (err) err.style.display = any ? "none" : "block";
      if (!any) ok = false;
    });
    if (!ok) {
      const first = $(".invalid", scope);
      first && first.scrollIntoView({ behavior: "smooth", block: "center" });
    }
    return ok;
  };
  document.addEventListener("input", (e) => {
    const f = e.target.closest && e.target.closest(".field.invalid");
    f && f.classList.remove("invalid");
  });

  /* ---------- آپلود فایل (ایمن + قابلیت حذف فایل) ---------- */
  $$(".upload").forEach((up) => {
    const input = $("input[type=file]", up);
    const list = up.nextElementSibling && up.nextElementSibling.classList.contains("upload-list") ? up.nextElementSibling : null;
    let selectedFiles = [];

    const syncFiles = () => {
      if (typeof DataTransfer !== "undefined") {
        const dt = new DataTransfer();
        selectedFiles.forEach((f) => dt.items.add(f));
        input.files = dt.files;
      }
    };
    const render = () => {
      if (!list) return;
      list.innerHTML = selectedFiles
        .map(
          (f, i) =>
            `<li><span>${esc(f.name)} <small class="muted">(${(f.size / 1024).toFixed(0)} KB)</small></span><button type="button" data-rm="${i}" aria-label="حذف فایل">✕</button></li>`
        )
        .join("");
      $$("[data-rm]", list).forEach((btn) =>
        btn.addEventListener("click", (ev) => {
          ev.stopPropagation();
          selectedFiles.splice(+btn.dataset.rm, 1);
          syncFiles();
          render();
        })
      );
    };
    up.addEventListener("click", () => input.click());
    input.addEventListener("change", () => {
      selectedFiles = [...selectedFiles, ...input.files];
      syncFiles();
      render();
    });
    ["dragenter", "dragover"].forEach((ev) =>
      up.addEventListener(ev, (e) => {
        e.preventDefault();
        up.classList.add("drag");
      })
    );
    ["dragleave", "drop"].forEach((ev) =>
      up.addEventListener(ev, (e) => {
        e.preventDefault();
        up.classList.remove("drag");
      })
    );
    up.addEventListener("drop", (e) => {
      selectedFiles = [...selectedFiles, ...e.dataTransfer.files];
      syncFiles();
      render();
    });
  });

  /* ---------- فرم چندمرحله‌ای سفارش ---------- */
  const orderForm = $("#order-form");
  if (orderForm) {
    const panes = $$(".step-pane", orderForm);
    const steps = $$(".stepper .s");
    const prevBtn = $("[data-prev]", orderForm),
      nextBtn = $("[data-next]", orderForm),
      submitBtn = $("[data-submit]", orderForm);
    let cur = 0;

    // پیش‌مقداردهی هوشمند از Query String (مثلاً از ماشین‌حساب یا بسته‌ها)
    const params = new URLSearchParams(location.search);
    const qService = params.get("service");
    const qPages = params.get("pages");
    if (qService) {
      const radio = $(`input[name=service][value="${CSS.escape(qService)}"]`, orderForm);
      if (radio) radio.checked = true;
    }
    if (qPages && +qPages > 0 && $("#pages", orderForm)) {
      $("#pages", orderForm).value = +qPages;
    }

    const PRICES = {
      cover: { base: 3500000, label: "طراحی جلد" },
      layout: { perPage: 18000, label: "صفحه‌آرایی" },
      both: { base: 3000000, perPage: 16000, label: "جلد + صفحه‌آرایی" },
      magazine: { perPage: 45000, label: "صفحه‌آرایی مجله" },
      ebook: { perPage: 12000, label: "کتاب الکترونیک" },
    };
    const urgency = { normal: 1, fast: 1.3, urgent: 1.6 };

    const estimate = () => {
      const svc = ($("input[name=service]:checked", orderForm) || {}).value;
      const pages = +($("#pages", orderForm).value || 0);
      const urg = $("#urgency", orderForm).value || "normal";
      if (!svc || !PRICES[svc]) return 0;
      const p = PRICES[svc];
      const total = (p.base || 0) + (p.perPage || 0) * pages;
      return Math.round((total * urgency[urg]) / 10000) * 10000;
    };
    const renderEstimate = () => {
      const el = $("#estimate");
      const v = estimate();
      el.textContent = v ? fa(v) + " تومان" : "—";
    };
    orderForm.addEventListener("change", renderEstimate);
    orderForm.addEventListener("input", renderEstimate);

    const go = (n) => {
      panes[cur].classList.remove("active");
      cur = n;
      panes[cur].classList.add("active");
      steps.forEach((s, i) => {
        s.classList.toggle("active", i === cur);
        s.classList.toggle("done", i < cur);
      });
      prevBtn.classList.toggle("hidden", cur === 0);
      nextBtn.classList.toggle("hidden", cur === panes.length - 1);
      submitBtn.classList.toggle("hidden", cur !== panes.length - 1);
      if (cur === panes.length - 1) fillSummary();
      orderForm.scrollIntoView({ behavior: "smooth", block: "start" });
    };
    const fillSummary = () => {
      const g = (n) => {
        const el = orderForm.elements[n];
        if (!el) return "—";
        if (el.tagName === "SELECT") return el.options[el.selectedIndex].text;
        return el.value.trim() || "—";
      };
      const svc = $("input[name=service]:checked", orderForm);
      const svcTitle = svc ? svc.closest(".choice").querySelector("b").textContent : "—";
      const pagesVal = g("pages");
      const s = $("#summary");
      s.innerHTML = `
        <dt>نوع خدمت</dt><dd>${esc(svcTitle)}</dd>
        <dt>عنوان اثر</dt><dd>${esc(g("title"))}</dd>
        <dt>ژانر</dt><dd>${esc(g("genre"))}</dd>
        <dt>تعداد صفحات</dt><dd>${pagesVal === "—" ? "—" : esc(fa(+pagesVal))}</dd>
        <dt>قطع</dt><dd>${esc(g("size"))}</dd>
        <dt>زمان تحویل</dt><dd>${esc(g("urgency"))}</dd>
        <dt>نام</dt><dd>${esc(g("name"))}</dd>
        <dt>تماس</dt><dd style="direction:ltr;text-align:right">${esc(g("phone"))}</dd>
        <dt>برآورد اولیه</dt><dd style="color:var(--c-teal);font-weight:800">${esc($("#estimate").textContent)}</dd>`;
    };
    nextBtn.addEventListener("click", () => {
      if (validateFields(panes[cur])) go(cur + 1);
    });
    prevBtn.addEventListener("click", () => go(cur - 1));
    orderForm.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!validateFields(panes[cur])) return;
      submitBtn.disabled = true;
      submitBtn.textContent = "در حال ارسال…";
      setTimeout(() => {
        const code = "AF-" + Math.floor(100000 + Math.random() * 900000);
        $("#order-success .code").textContent = code;
        $("#order-wrap").classList.add("hidden");
        $("#order-success").classList.remove("hidden");
        window.scrollTo({ top: 0, behavior: "smooth" });
      }, 1100);
    });
    renderEstimate();
  }

  /* ---------- فرم مشاوره ---------- */
  const consultForm = $("#consult-form");
  if (consultForm) {
    const qMode = new URLSearchParams(location.search).get("mode");
    if (qMode) {
      const mRadio = $(`input[name=type][value="${CSS.escape(qMode)}"]`, consultForm);
      if (mRadio) mRadio.checked = true;
    }
    const daysEl = $(".days", consultForm);
    const fmtDay = new Intl.DateTimeFormat("fa-IR-u-ca-persian", { day: "numeric" });
    const fmtWd = new Intl.DateTimeFormat("fa-IR-u-ca-persian", { weekday: "short" });
    const fmtMon = new Intl.DateTimeFormat("fa-IR-u-ca-persian", { month: "long" });
    const fmtFull = new Intl.DateTimeFormat("fa-IR-u-ca-persian", { weekday: "long", day: "numeric", month: "long" });
    let d = new Date(),
      added = 0,
      sel = null;
    while (added < 10) {
      d.setDate(d.getDate() + 1);
      if (d.getDay() === 5) continue;
      const b = document.createElement("button");
      b.type = "button";
      b.className = "day";
      b.dataset.date = d.toISOString();
      b.innerHTML = `<small>${fmtWd.format(d)}</small><b>${fmtDay.format(d)}</b><small>${fmtMon.format(d)}</small>`;
      b.addEventListener("click", () => {
        $$(".day", daysEl).forEach((x) => x.classList.remove("active"));
        b.classList.add("active");
        sel = new Date(b.dataset.date);
        $("#sel-date").value = fmtFull.format(sel);
        renderSlots();
      });
      daysEl.appendChild(b);
      added++;
    }
    const slotsEl = $(".slots", consultForm);
    const renderSlots = () => {
      slotsEl.innerHTML = "";
      ["۱۰:۰۰", "۱۱:۰۰", "۱۲:۰۰", "۱۴:۰۰", "۱۵:۰۰", "۱۶:۰۰", "۱۷:۰۰", "۱۸:۰۰"].forEach((t, i) => {
        const b = document.createElement("button");
        b.type = "button";
        b.className = "slot";
        b.textContent = t;
        if ((sel.getDate() + i) % 4 === 0) b.classList.add("off");
        b.addEventListener("click", () => {
          $$(".slot", slotsEl).forEach((x) => x.classList.remove("active"));
          b.classList.add("active");
          $("#sel-time").value = t;
        });
        slotsEl.appendChild(b);
      });
    };
    $$(".day", daysEl)[0].click();
    consultForm.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!validateFields(consultForm)) return;
      if (!$("#sel-time").value) {
        toast("لطفاً یک ساعت برای مشاوره انتخاب کنید");
        return;
      }
      const btn = $("[type=submit]", consultForm);
      btn.disabled = true;
      btn.textContent = "در حال ثبت…";
      setTimeout(() => {
        $("#consult-wrap").classList.add("hidden");
        $("#consult-success").classList.remove("hidden");
        $("#consult-success [data-when]").textContent = $("#sel-date").value + " — ساعت " + $("#sel-time").value;
        window.scrollTo({ top: 0, behavior: "smooth" });
      }, 1000);
    });
  }

  /* ---------- فرم تماس / خبرنامه ---------- */
  $$("form[data-simple]").forEach((f) => {
    f.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!validateFields(f)) return;
      const btn = $("[type=submit]", f);
      const t = btn.textContent;
      btn.disabled = true;
      btn.textContent = "در حال ارسال…";
      setTimeout(() => {
        btn.disabled = false;
        btn.textContent = t;
        f.reset();
        toast(f.dataset.simple || "پیام شما با موفقیت ارسال شد ✅");
      }, 900);
    });
  });

  /* ---------- ماشین‌حساب قیمت در صفحه خدمات ---------- */
  const calc = $("#calc");
  if (calc) {
    const out = $("#calc-out");
    const orderLink = $("[data-calc-order]", calc.parentElement);
    const run = () => {
      const type = calc.elements.type.value,
        pages = +calc.elements.pages.value || 0,
        cover = calc.elements.cover.checked,
        edit = calc.elements.edit.checked;
      const per = { book: 18000, academic: 22000, magazine: 45000, kids: 60000, ebook: 12000 }[type];
      const total = per * pages + (cover ? 3500000 : 0) + (edit ? pages * 6000 : 0);
      out.textContent = total ? fa(Math.round(total / 10000) * 10000) + " تومان" : "—";
      if (orderLink) {
        const svcMap = {
          book: cover ? "both" : "layout",
          academic: cover ? "both" : "layout",
          kids: cover ? "both" : "layout",
          magazine: "magazine",
          ebook: "ebook",
        };
        orderLink.href = `order.html?service=${svcMap[type] || "both"}&pages=${pages}`;
      }
    };
    calc.addEventListener("input", run);
    calc.addEventListener("change", run);
    run();
  }

  /* ---------- سال جاری شمسی ---------- */
  $$("[data-year]").forEach(
    (el) => (el.textContent = new Intl.DateTimeFormat("fa-IR-u-ca-persian", { year: "numeric" }).format(new Date()))
  );
})();
