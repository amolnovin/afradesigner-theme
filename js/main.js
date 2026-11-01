/* =====================================================
   افرا گرافیک — اسکریپت اصلی
   ===================================================== */
(function () {
  "use strict";

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];

  /* ---------- تم (روشن/تاریک) ---------- */
  const root = document.documentElement;
  const savedTheme = localStorage.getItem("afra-theme");
  root.dataset.theme = savedTheme || "auto";
  $$("[data-theme-toggle]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const isDark =
        root.dataset.theme === "dark" ||
        (root.dataset.theme === "auto" && matchMedia("(prefers-color-scheme: dark)").matches);
      root.dataset.theme = isDark ? "light" : "dark";
      localStorage.setItem("afra-theme", root.dataset.theme);
    });
  });

  /* ---------- هدر چسبان ---------- */
  const header = $(".header");
  const toTop = $(".to-top");
  const onScroll = () => {
    const y = window.scrollY;
    header && header.classList.toggle("scrolled", y > 10);
    toTop && toTop.classList.toggle("show", y > 500);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  toTop && toTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));

  /* ---------- منوی موبایل ---------- */
  const mm = $(".mobile-menu");
  $$("[data-menu-open]").forEach((b) => b.addEventListener("click", () => { mm.classList.add("open"); document.body.style.overflow = "hidden"; }));
  $$("[data-menu-close]").forEach((b) => b.addEventListener("click", () => { mm.classList.remove("open"); document.body.style.overflow = ""; }));

  /* ---------- لینک فعال ---------- */
  const current = location.pathname.split("/").pop() || "index.html";
  $$(".nav-links a, .mobile-menu nav a").forEach((a) => {
    if (a.getAttribute("href") === current) a.classList.add("active");
  });

  /* ---------- انیمیشن ورود ---------- */
  const io = new IntersectionObserver(
    (entries) => entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }),
    { threshold: 0.12 }
  );
  $$(".reveal, .skill").forEach((el) => io.observe(el));

  /* ---------- شمارنده اعداد ---------- */
  const fa = (n) => n.toLocaleString("fa-IR");
  const cio = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      const el = e.target, target = +el.dataset.count, suffix = el.dataset.suffix || "";
      const dur = 1600, t0 = performance.now();
      const tick = (t) => {
        const p = Math.min(1, (t - t0) / dur), v = Math.round(target * (1 - Math.pow(1 - p, 3)));
        el.textContent = fa(v) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
      cio.unobserve(el);
    });
  }, { threshold: 0.5 });
  $$("[data-count]").forEach((el) => cio.observe(el));

  /* ---------- Toast ---------- */
  let toastEl = $(".toast");
  if (!toastEl) { toastEl = document.createElement("div"); toastEl.className = "toast"; document.body.appendChild(toastEl); }
  let toastT;
  window.toast = (msg) => {
    toastEl.textContent = msg; toastEl.classList.add("show");
    clearTimeout(toastT); toastT = setTimeout(() => toastEl.classList.remove("show"), 3200);
  };

  /* ---------- فیلتر نمونه‌کار + لایت‌باکس ---------- */
  const workGrid = $(".work-grid");
  if (workGrid) {
    const works = $$(".work", workGrid);
    $$(".filter-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        $$(".filter-btn").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        const f = btn.dataset.filter;
        works.forEach((w) => w.classList.toggle("hide", f !== "all" && w.dataset.cat !== f));
      });
    });

    // لایت‌باکس
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
          <a href="order.html" class="btn btn-primary" style="margin-top:auto">سفارش پروژه مشابه</a>
        </div>
      </div>`;
    document.body.appendChild(lb);
    let idx = 0;
    const visible = () => works.filter((w) => !w.classList.contains("hide"));
    const show = (i) => {
      const list = visible(); idx = (i + list.length) % list.length;
      const w = list[idx], d = w.dataset;
      $("img", lb).src = $("img", w).src;
      $("[data-lb=cat]", lb).textContent = d.catLabel || "";
      $("[data-lb=title]", lb).textContent = d.title || "";
      $("[data-lb=desc]", lb).textContent = d.desc || "";
      $("[data-lb=meta]", lb).innerHTML = (d.meta || "").split("|").filter(Boolean).map((m) => `<span>${m.trim()}</span>`).join("");
      lb.classList.add("open"); document.body.style.overflow = "hidden";
    };
    const close = () => { lb.classList.remove("open"); document.body.style.overflow = ""; };
    works.forEach((w) => w.addEventListener("click", () => show(visible().indexOf(w))));
    $(".lightbox-close", lb).addEventListener("click", close);
    $(".prev", lb).addEventListener("click", () => show(idx - 1));
    $(".next", lb).addEventListener("click", () => show(idx + 1));
    lb.addEventListener("click", (e) => { if (e.target === lb) close(); });
    document.addEventListener("keydown", (e) => {
      if (!lb.classList.contains("open")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowRight") show(idx - 1);
      if (e.key === "ArrowLeft") show(idx + 1);
    });
  }

  /* ---------- اسلایدر نظرات ---------- */
  const tt = $(".testi-track");
  if (tt) {
    $$("[data-testi]").forEach((b) => b.addEventListener("click", () => {
      const dir = b.dataset.testi === "next" ? -1 : 1;
      tt.scrollBy({ left: dir * 400, behavior: "smooth" });
    }));
  }

  /* ---------- اعتبارسنجی فرم عمومی ---------- */
  const validateFields = (scope) => {
    let ok = true;
    $$("[required]", scope).forEach((inp) => {
      const field = inp.closest(".field");
      let valid = inp.type === "checkbox" ? inp.checked : inp.value.trim() !== "";
      if (valid && inp.type === "email") valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(inp.value);
      if (valid && inp.type === "tel") valid = /^(\+98|0)?9\d{9}$/.test(inp.value.replace(/[\s-]/g, "").replace(/[۰-۹]/g, (d) => "۰۱۲۳۴۵۶۷۸۹".indexOf(d)));
      field && field.classList.toggle("invalid", !valid);
      if (!valid) ok = false;
    });
    // گروه‌های رادیویی
    $$("[data-required-group]", scope).forEach((g) => {
      const any = $$("input:checked", g).length > 0;
      g.classList.toggle("invalid", !any);
      const err = $(".err", g); if (err) err.style.display = any ? "none" : "block";
      if (!any) ok = false;
    });
    if (!ok) { const first = $(".invalid", scope); first && first.scrollIntoView({ behavior: "smooth", block: "center" }); }
    return ok;
  };
  document.addEventListener("input", (e) => {
    const f = e.target.closest && e.target.closest(".field.invalid");
    f && f.classList.remove("invalid");
  });

  /* ---------- آپلود فایل (نمایشی) ---------- */
  $$(".upload").forEach((up) => {
    const input = $("input[type=file]", up);
    const list = up.nextElementSibling && up.nextElementSibling.classList.contains("upload-list") ? up.nextElementSibling : null;
    const render = () => {
      if (!list) return;
      list.innerHTML = [...input.files].map((f, i) => `<li><span>${f.name} <small class="muted">(${(f.size / 1024).toFixed(0)} KB)</small></span></li>`).join("");
    };
    up.addEventListener("click", () => input.click());
    input.addEventListener("change", render);
    ["dragenter", "dragover"].forEach((ev) => up.addEventListener(ev, (e) => { e.preventDefault(); up.classList.add("drag"); }));
    ["dragleave", "drop"].forEach((ev) => up.addEventListener(ev, (e) => { e.preventDefault(); up.classList.remove("drag"); }));
    up.addEventListener("drop", (e) => { input.files = e.dataTransfer.files; render(); });
  });

  /* ---------- فرم چندمرحله‌ای سفارش ---------- */
  const orderForm = $("#order-form");
  if (orderForm) {
    const panes = $$(".step-pane", orderForm);
    const steps = $$(".stepper .s");
    const prevBtn = $("[data-prev]", orderForm), nextBtn = $("[data-next]", orderForm), submitBtn = $("[data-submit]", orderForm);
    let cur = 0;

    // قیمت پایه (تومان) — قابل تغییر
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
      if (!svc) return 0;
      const p = PRICES[svc];
      let total = (p.base || 0) + (p.perPage || 0) * pages;
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
      steps.forEach((s, i) => { s.classList.toggle("active", i === cur); s.classList.toggle("done", i < cur); });
      prevBtn.classList.toggle("hidden", cur === 0);
      nextBtn.classList.toggle("hidden", cur === panes.length - 1);
      submitBtn.classList.toggle("hidden", cur !== panes.length - 1);
      if (cur === panes.length - 1) fillSummary();
      orderForm.scrollIntoView({ behavior: "smooth", block: "start" });
    };
    const fillSummary = () => {
      const g = (n) => { const el = orderForm.elements[n]; if (!el) return "—"; if (el.tagName === "SELECT") return el.options[el.selectedIndex].text; return el.value || "—"; };
      const svc = $("input[name=service]:checked", orderForm);
      const s = $("#summary");
      s.innerHTML = `
        <dt>نوع خدمت</dt><dd>${svc ? svc.closest(".choice").querySelector("b").textContent : "—"}</dd>
        <dt>عنوان اثر</dt><dd>${g("title")}</dd>
        <dt>ژانر</dt><dd>${g("genre")}</dd>
        <dt>تعداد صفحات</dt><dd>${g("pages") === "—" ? "—" : fa(+g("pages"))}</dd>
        <dt>قطع</dt><dd>${g("size")}</dd>
        <dt>زمان تحویل</dt><dd>${g("urgency")}</dd>
        <dt>نام</dt><dd>${g("name")}</dd>
        <dt>تماس</dt><dd style="direction:ltr;text-align:right">${g("phone")}</dd>
        <dt>برآورد اولیه</dt><dd style="color:var(--c-teal);font-weight:800">${$("#estimate").textContent}</dd>`;
    };
    nextBtn.addEventListener("click", () => { if (validateFields(panes[cur])) go(cur + 1); });
    prevBtn.addEventListener("click", () => go(cur - 1));
    orderForm.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!validateFields(panes[cur])) return;
      submitBtn.disabled = true; submitBtn.textContent = "در حال ارسال…";
      // در نسخه نهایی این‌جا داده‌ها به سرور/فرم‌ساز ارسال می‌شود (fetch به API یا وردپرس)
      setTimeout(() => {
        const code = "AF-" + Math.floor(100000 + Math.random() * 900000);
        $("#order-success .code").textContent = code;
        $("#order-wrap").classList.add("hidden");
        $("#order-success").classList.remove("hidden");
        window.scrollTo({ top: 0, behavior: "smooth" });
      }, 1200);
    });
    renderEstimate();
  }

  /* ---------- فرم مشاوره ---------- */
  const consultForm = $("#consult-form");
  if (consultForm) {
    // روزهای آینده (تقویم شمسی با Intl)
    const daysEl = $(".days", consultForm);
    const fmtDay = new Intl.DateTimeFormat("fa-IR-u-ca-persian", { day: "numeric" });
    const fmtWd = new Intl.DateTimeFormat("fa-IR-u-ca-persian", { weekday: "short" });
    const fmtMon = new Intl.DateTimeFormat("fa-IR-u-ca-persian", { month: "long" });
    const fmtFull = new Intl.DateTimeFormat("fa-IR-u-ca-persian", { weekday: "long", day: "numeric", month: "long" });
    let d = new Date(), added = 0, sel = null;
    while (added < 10) {
      d.setDate(d.getDate() + 1);
      if (d.getDay() === 5) continue; // جمعه تعطیل
      const b = document.createElement("button");
      b.type = "button"; b.className = "day"; b.dataset.date = d.toISOString();
      b.innerHTML = `<small>${fmtWd.format(d)}</small><b>${fmtDay.format(d)}</b><small>${fmtMon.format(d)}</small>`;
      b.addEventListener("click", () => {
        $$(".day", daysEl).forEach((x) => x.classList.remove("active")); b.classList.add("active");
        sel = new Date(b.dataset.date); $("#sel-date").value = fmtFull.format(sel);
        renderSlots();
      });
      daysEl.appendChild(b); added++;
    }
    const slotsEl = $(".slots", consultForm);
    const renderSlots = () => {
      slotsEl.innerHTML = "";
      ["۱۰:۰۰", "۱۱:۰۰", "۱۲:۰۰", "۱۴:۰۰", "۱۵:۰۰", "۱۶:۰۰", "۱۷:۰۰", "۱۸:۰۰"].forEach((t, i) => {
        const b = document.createElement("button"); b.type = "button"; b.className = "slot"; b.textContent = t;
        // شبیه‌سازی زمان‌های پر
        if ((sel.getDate() + i) % 4 === 0) b.classList.add("off");
        b.addEventListener("click", () => { $$(".slot", slotsEl).forEach((x) => x.classList.remove("active")); b.classList.add("active"); $("#sel-time").value = t; });
        slotsEl.appendChild(b);
      });
    };
    $$(".day", daysEl)[0].click();
    consultForm.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!validateFields(consultForm)) return;
      if (!$("#sel-time").value) { toast("لطفاً یک ساعت برای مشاوره انتخاب کنید"); return; }
      const btn = $("[type=submit]", consultForm); btn.disabled = true; btn.textContent = "در حال ثبت…";
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
      const btn = $("[type=submit]", f); const t = btn.textContent; btn.disabled = true; btn.textContent = "در حال ارسال…";
      setTimeout(() => { btn.disabled = false; btn.textContent = t; f.reset(); toast(f.dataset.simple || "پیام شما با موفقیت ارسال شد ✅"); }, 900);
    });
  });

  /* ---------- ماشین‌حساب قیمت در صفحه خدمات ---------- */
  const calc = $("#calc");
  if (calc) {
    const out = $("#calc-out");
    const run = () => {
      const type = calc.elements.type.value, pages = +calc.elements.pages.value || 0, cover = calc.elements.cover.checked, edit = calc.elements.edit.checked;
      const per = { book: 18000, academic: 22000, magazine: 45000, kids: 60000, ebook: 12000 }[type];
      let total = per * pages + (cover ? 3500000 : 0) + (edit ? pages * 6000 : 0);
      out.textContent = total ? fa(Math.round(total / 10000) * 10000) + " تومان" : "—";
    };
    calc.addEventListener("input", run); calc.addEventListener("change", run); run();
  }

  /* ---------- سال جاری ---------- */
  $$("[data-year]").forEach((el) => el.textContent = new Intl.DateTimeFormat("fa-IR-u-ca-persian", { year: "numeric" }).format(new Date()));
})();
