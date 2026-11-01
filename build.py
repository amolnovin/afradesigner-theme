# -*- coding: utf-8 -*-
"""
اسکریپت ساخت صفحات استاتیک قالب پرسونال برندینگ «افرا حسین‌زاده»
اجرا:  python3 build.py
هدر، کشوی منوی همبرگری، جستجوی هوشمند، نوار دک پایین صفحه و فوتر مشترک را در همه صفحات تولید می‌کند.
"""
import os

ICONS = {
    "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>',
    "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    "grid": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="7" height="7" x="3" y="3" rx="1.5"/><rect width="7" height="7" x="14" y="3" rx="1.5"/><rect width="7" height="7" x="14" y="14" rx="1.5"/><rect width="7" height="7" x="3" y="14" rx="1.5"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/></svg>',
    "compass": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2"/><line x1="16" x2="16" y1="2" y2="6"/><line x1="8" x2="8" y1="2" y2="6"/><line x1="3" x2="21" y1="10" y2="10"/><path d="M8 14h.01M12 14h.01M16 14h.01M8 18h.01M12 18h.01"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/></svg>',
    "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
    "moon": '<svg class="ic-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>',
    "sun": '<svg class="ic-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="m12 19-7-7 7-7"/></svg>',
    "arrow_r": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg>',
    "layout": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18M9 21V9"/></svg>',
    "mag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 6h4M2 10h4M2 14h4M2 18h4"/><rect width="16" height="20" x="4" y="2" rx="2"/><path d="M15 2v20M9 7h3M9 11h3"/></svg>',
    "tablet": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="20" x="4" y="2" rx="2"/><path d="M12 18h.01"/></svg>',
    "edit": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>',
    "print": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect width="12" height="8" x="6" y="14"/></svg>',
    "upload": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m17 8-5-5-5 5M12 3v12"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h12M4 17h16"/></svg>',
    "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4M12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 0 1 2.2 12C2.2 6.6 6.6 2.2 12 2.2S21.8 6.6 21.8 12 17.4 21.8 12 21.8M12 0C5.4 0 0 5.4 0 12c0 2.1.6 4.2 1.6 6L0 24l6.2-1.6c1.8 1 3.8 1.5 5.8 1.5 6.6 0 12-5.4 12-12S18.6 0 12 0"/></svg>',
    "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="20" x="2" y="2" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/></svg>',
    "tg": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.4 18.7 19.6c-.2 1-.9 1.3-1.8.8l-5-3.7-2.4 2.3c-.3.3-.5.5-1 .5l.4-5.1L18 6.1c.4-.4-.1-.6-.6-.2L5.9 13.1 1 11.6c-1.1-.3-1.1-1.1.2-1.6L20.5 2.6c.9-.3 1.7.2 1.4 1.8"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9v5.7H9.3V9h3.4v1.6c.5-.9 1.6-1.8 3.4-1.8 3.6 0 4.3 2.4 4.3 5.5v6.2ZM5.3 7.4a2.1 2.1 0 1 1 0-4.1 2.1 2.1 0 0 1 0 4.1M7.1 20.5H3.5V9h3.6ZM22.2 0H1.8C.8 0 0 .8 0 1.7v20.5c0 1 .8 1.8 1.8 1.8h20.4c1 0 1.8-.8 1.8-1.8V1.7C24 .8 23.2 0 22.2 0"/></svg>',
    "up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m18 15-6-6-6 6"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    "video": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m22 8-6 4 6 4V8Z"/><rect width="14" height="12" x="2" y="6" rx="2"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "bag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"/><path d="M3 6h18"/><path d="M16 10a4 4 0 0 1-8 0"/></svg>',
}

# منوی کامل سایت (قرارگرفته در کشوی همبرگری گوشه سمت چپ)
NAV = [
    ("index.html", "خانه و معرفی برند", "home"),
    ("services.html", "خدمات و تعرفه‌ها", "layers"),
    ("portfolio.html", "گالری نمونه‌کارها", "book"),
    ("order.html", "ثبت سفارش آنلاین", "bag"),
    ("consult.html", "رزرو مشاوره رایگان", "calendar"),
    ("about.html", "درباره افرا حسین‌زاده", "user"),
    ("blog.html", "مجله تخصصی نشر", "doc"),
    ("contact.html", "تماس با من", "phone"),
]

# بخش‌های نوار دک پایین صفحه (الهام‌گرفته از سایدبار ehsanamirian.com منتقل‌شده به پایین صفحه)
DOCK_SECTIONS = [
    ("hero", "معرفی", "home"),
    ("hub", "اکوسیستم", "grid"),
    ("about", "درباره افرا", "user"),
    ("services", "خدمات", "layers"),
    ("portfolio", "نمونه‌کارها", "book"),
    ("process", "فرآیند کار", "compass"),
    ("consult", "رزرو مشاوره", "calendar"),
    ("testimonials", "نظرات", "star"),
    ("blog", "مجله", "doc"),
    ("contact", "تماس", "phone"),
]


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | افرا حسین‌زاده — طراح جلد و صفحه‌آرایی کتاب</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#11694e">
<meta property="og:title" content="{title} | افرا حسین‌زاده">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/afra-hosseinzadeh.png">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%2311694e'/%3E%3Cpath d='M32 50A18 18 0 0 1 29 14c14-3 18-4 23-10 2 5 5 10 5 20 0 14-12 26-25 26Z' fill='%23fff'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<script>(function(){{try{{var t=localStorage.getItem("afra-theme");document.documentElement.dataset.theme=t||"dark";}}catch(e){{}}}})();</script>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="dock-progress" aria-hidden="true"></div>
<div class="sec-transition-veil" aria-hidden="true"></div>
"""


def header():
    mlinks = "".join(
        f'<a href="{h}"><span class="link-main">{ICONS[ic]}<span>{t}</span></span><span class="arr">{ICONS["arrow"]}</span></a>'
        for h, t, ic in NAV
    )
    return f"""
<header class="header">
  <div class="container nav">
    <a href="index.html" class="logo" aria-label="افرا حسین‌زاده — صفحه اصلی">
      <span class="logo-mark">{ICONS["leaf"]}</span>
      <span class="logo-text"><b>افرا حسین‌زاده</b><small>طراح جلد کتاب و مدیر هنری صفحه‌آرایی</small></span>
    </a>
    <div class="nav-actions">
      <button type="button" class="search-btn" data-search-open aria-label="جستجو در سایت">
        {ICONS["search"]}
        <span>جستجو</span>
        <kbd>Ctrl K</kbd>
      </button>
      <button type="button" class="icon-btn theme-toggle" data-theme-toggle aria-label="تغییر حالت روشن و تاریک">
        {ICONS["sun"]}{ICONS["moon"]}
      </button>
      <button type="button" class="burger-btn" data-menu-open aria-label="باز کردن منوی فهرست صفحات">
        {ICONS["menu"]}
        <span>منو</span>
      </button>
    </div>
  </div>
</header>

<div class="drawer-backdrop" aria-hidden="true"></div>
<aside class="nav-drawer" aria-hidden="true" aria-label="منوی اصلی سایت">
  <div class="top">
    <a href="index.html" class="logo">
      <span class="logo-mark">{ICONS["leaf"]}</span>
      <span class="logo-text"><b>افرا حسین‌زاده</b><small>برند شخصی طراحی و نشر</small></span>
    </a>
    <button type="button" class="icon-btn" data-menu-close aria-label="بستن منو">{ICONS["x"]}</button>
  </div>
  <div class="drawer-profile">
    <img src="assets/afra-hosseinzadeh.png" alt="افرا حسین‌زاده" width="614" height="820">
    <div>
      <b>افرا حسین‌زاده</b>
      <small>۱۰+ سال تجربه • +۴۵۰ کتاب منتشرشده</small>
    </div>
  </div>
  <div class="drawer-lbl">دسترسی به صفحات قالب</div>
  <nav>{mlinks}</nav>
  <div class="bottom">
    <a href="order.html" class="btn btn-primary btn-block">ثبت سفارش آنلاین پروژه</a>
    <a href="consult.html" class="btn btn-outline btn-block">رزرو جلسه مشاوره رایگان</a>
    <div class="drawer-socials">
      <a href="https://instagram.com" target="_blank" rel="noopener" aria-label="اینستاگرام">{ICONS["ig"]}</a>
      <a href="https://t.me" target="_blank" rel="noopener" aria-label="تلگرام">{ICONS["tg"]}</a>
      <a href="https://wa.me/989120000000" target="_blank" rel="noopener" aria-label="واتساپ">{ICONS["wa"]}</a>
      <a href="https://linkedin.com" target="_blank" rel="noopener" aria-label="لینکدین">{ICONS["linkedin"]}</a>
    </div>
  </div>
</aside>

<div class="search-modal" id="search-modal" aria-hidden="true" role="dialog" aria-label="جستجوی سایت">
  <div class="search-dialog">
    <div class="search-bar">
      {ICONS["search"]}
      <input type="search" id="search-input" placeholder="جستجو در خدمات، نمونه‌کارها، مقالات و بخش‌ها…" autocomplete="off">
      <button type="button" class="close-esc" data-search-close>ESC</button>
    </div>
    <div class="search-tags">
      <small>پیشنهاد سریع:</small>
      <button type="button" class="search-tag" data-search-tag="طراحی جلد">طراحی جلد</button>
      <button type="button" class="search-tag" data-search-tag="صفحه‌آرایی">صفحه‌آرایی</button>
      <button type="button" class="search-tag" data-search-tag="تعرفه">ماشین‌حساب تعرفه</button>
      <button type="button" class="search-tag" data-search-tag="مشاوره">مشاوره رایگان</button>
      <button type="button" class="search-tag" data-search-tag="EPUB">کتاب الکترونیک</button>
    </div>
    <div class="search-results" id="search-results"></div>
  </div>
</div>
<main>
"""


def bottom_dock(is_home=False):
    items = ""
    for i, (sec_id, label, icon) in enumerate(DOCK_SECTIONS):
        href = f"#{sec_id}" if is_home else f"index.html#{sec_id}"
        active_cls = " active" if (is_home and i == 0) else ""
        items += (
            f'<a href="{href}" class="dock-item{active_cls}" data-sec="{sec_id}" data-tooltip="{label}" aria-label="{label}">'
            f'{ICONS[icon]}<span class="dock-lbl">{label}</span></a>'
        )
    return f"""
<nav class="section-dock" aria-label="ناوبری سریع بخش‌ها">
  {items}
</nav>
"""


def footer(is_home=False):
    return f"""
</main>
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a href="index.html" class="logo">
          <span class="logo-mark">{ICONS["leaf"]}</span>
          <span class="logo-text"><b>افرا حسین‌زاده</b><small>طراح جلد و صفحه‌آرایی کتاب</small></span>
        </a>
        <p style="margin-top:1rem">بیش از ده سال همراهی تخصصی با ناشران معتبر و نویسندگان مستقل در خلق جلدهای ماندگار، صفحه‌آرایی استاندارد و آماده‌سازی دقیق چاپ. هر کتاب، یک معماری بصری یکتاست.</p>
        <div class="socials">
          <a href="https://instagram.com" target="_blank" rel="noopener" aria-label="اینستاگرام">{ICONS["ig"]}</a>
          <a href="https://t.me" target="_blank" rel="noopener" aria-label="تلگرام">{ICONS["tg"]}</a>
          <a href="https://wa.me/989120000000" target="_blank" rel="noopener" aria-label="واتساپ">{ICONS["wa"]}</a>
          <a href="https://linkedin.com" target="_blank" rel="noopener" aria-label="لینکدین">{ICONS["linkedin"]}</a>
        </div>
      </div>
      <div>
        <h4>دسترسی سریع</h4>
        <ul>
          <li><a href="services.html">خدمات و تعرفه‌ها</a></li>
          <li><a href="portfolio.html">نمونه‌کارها</a></li>
          <li><a href="order.html">ثبت سفارش آنلاین</a></li>
          <li><a href="consult.html">رزرو مشاوره رایگان</a></li>
          <li><a href="about.html">درباره افرا حسین‌زاده</a></li>
          <li><a href="blog.html">مجله تخصصی</a></li>
        </ul>
      </div>
      <div>
        <h4>تخصص‌ها</h4>
        <ul>
          <li><a href="services.html#cover">طراحی جلد کتاب</a></li>
          <li><a href="services.html#layout">صفحه‌آرایی در ایندیزاین</a></li>
          <li><a href="services.html#magazine">صفحه‌آرایی مجله و کاتالوگ</a></li>
          <li><a href="services.html#ebook">کتاب الکترونیک (EPUB)</a></li>
          <li><a href="services.html#print">آماده‌سازی فنی و نظارت چاپ</a></li>
        </ul>
      </div>
      <div>
        <h4>ارتباط مستقیم</h4>
        <ul class="contact-list">
          <li>{ICONS["phone"]}<a href="tel:+989120000000" dir="ltr">0912 000 0000</a></li>
          <li>{ICONS["mail"]}<a href="mailto:info@afradesigner.ir">info@afradesigner.ir</a></li>
          <li>{ICONS["clock"]}<span>شنبه تا پنج‌شنبه — ۱۰ تا ۱۸</span></li>
          <li>{ICONS["pin"]}<span>تهران — همکاری آنلاین با سراسر ایران و خارج از کشور</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year></span> افرا حسین‌زاده (استودیو افرا گرافیک) — تمامی حقوق محفوظ است.</span>
      <span>afradesigner.ir</span>
    </div>
  </div>
</footer>
{bottom_dock(is_home=is_home)}
<a href="https://wa.me/989120000000" class="fab-wa" target="_blank" rel="noopener" aria-label="گفتگو در واتساپ">{ICONS["wa"]}</a>
<button type="button" class="to-top" aria-label="بازگشت به بالا">{ICONS["up"]}</button>
<div class="toast" role="status"></div>
<script src="js/main.js"></script>
</body>
</html>
"""


def page_hero(crumb, title, lead):
    return f"""
<section class="page-hero text-center">
  <div class="container">
    <nav class="breadcrumb"><a href="index.html">افرا حسین‌زاده</a><span>/</span><span>{crumb}</span></nav>
    <h1>{title}</h1>
    <p>{lead}</p>
  </div>
</section>
"""


def cta_block():
    return f"""
<section class="section--tight">
  <div class="container">
    <div class="cta reveal">
      <h2>آماده‌اید کتاب‌تان را با هویتی ماندگار منتشر کنید؟</h2>
      <p>در کمتر از ۵ دقیقه سفارش طراحی جلد یا صفحه‌آرایی خود را ثبت کنید، یا یک جلسه مشاوره رایگان ۲۰ دقیقه‌ای با افرا حسین‌زاده رزرو نمایید.</p>
      <div class="actions">
        <a href="order.html" class="btn btn-primary btn-lg">ثبت سفارش آنلاین</a>
        <a href="consult.html" class="btn btn-outline btn-lg">مشاوره رایگان با افرا</a>
      </div>
    </div>
  </div>
</section>
"""


WORKS = [
    ("cover-1.jpg", "cover", "طراحی جلد", "رمان «برگ‌های ارغوانی»", "طراحی جلد رمان ادبی با تصویرسازی برگ افرا و تایپوگرافی طلایی", "نشر نگاه | جلد سخت | رقعی | ۱۴۰۳", False),
    ("layout-1.jpg", "layout", "صفحه‌آرایی", "صفحه‌آرایی مجموعه داستان", "طراحی گرید دو ستونه، سرفصل‌های تزئینی و حاشیه‌های استاندارد چاپ", "نشر چشمه | ۳۲۰ صفحه | وزیری | ایندیزاین", True),
    ("cover-2.jpg", "cover", "طراحی جلد", "دفتر شعر «پرنده و پنجره»", "جلد مینیمال با فرم‌های هندسی و خط‌نگاره پرنده", "نشر مروارید | شومیز | رقعی | ۱۴۰۲", False),
    ("cover-3.jpg", "kids", "کتاب کودک", "قصه‌ی روباه و ماه", "تصویرسازی آبرنگی و لترینگ کودکانه برای گروه سنی ب", "کانون پرورش فکری | خشتی | ۱۴۰۳", False),
    ("cover-4.jpg", "academic", "دانشگاهی", "روان‌شناسی شناختی", "طراحی جلد کتاب درسی با هویت بصری آکادمیک و مدرن", "انتشارات سمت | وزیری | چاپ سوم", False),
    ("layout-2.jpg", "magazine", "مجله", "ماهنامه هنر و اندیشه", "صفحه‌آرایی ادیتوریال با گرید چندستونه و نقل‌قول‌های برجسته", "۹۶ صفحه | A4 | گلاسه | ۱۴۰۳", True),
]


def work_cards(limit=None):
    items = WORKS if limit is None else WORKS[:limit]
    out = ""
    for i, (img, cat, cat_label, title, desc, meta, wide) in enumerate(items):
        out += f"""
      <article class="work reveal{" wide" if wide else ""}" data-cat="{cat}" data-cat-label="{cat_label}" data-title="{title}" data-desc="{desc}" data-meta="{meta}" data-delay="{i % 3}">
        <img src="assets/{img}" alt="{title}" loading="lazy">
        <div class="work-info"><span class="tag">{cat_label}</span><h3>{title}</h3><p>{meta.split('|')[0].strip()}</p></div>
      </article>"""
    return out


FILTERS = [("all", "همه"), ("cover", "طراحی جلد"), ("layout", "صفحه‌آرایی"), ("magazine", "مجله"), ("kids", "کودک"), ("academic", "دانشگاهی")]


def filters():
    return "".join(f'<button type="button" class="filter-btn{" active" if k=="all" else ""}" data-filter="{k}">{v}</button>' for k, v in FILTERS)


BLOG_POSTS = [
    ("layout-1.jpg", "edu", "آموزش", "۱۰ اشتباه رایج در صفحه‌آرایی کتاب فارسی", "از کشیدگی‌های نابه‌جا تا فاصله‌ی خطوط اشتباه؛ اشتباهاتی که خوانایی کتاب را از بین می‌برند.", "۷ دقیقه", "۱۲ شهریور ۱۴۰۴"),
    ("cover-1.jpg", "cover", "طراحی جلد", "جلد کتاب چطور فروش را تغییر می‌دهد؟", "خواننده در ۳ ثانیه تصمیم می‌گیرد کتاب را بردارد یا نه. جلد، اولین و مهم‌ترین سفیر بصری کتاب شماست.", "۵ دقیقه", "۲ شهریور ۱۴۰۴"),
    ("cover-4.jpg", "pub", "راهنمای نشر", "راهنمای کامل چاپ اولین کتاب برای نویسندگان مستقل", "از ویرایش و شابک تا انتخاب کاغذ و چاپخانه؛ همه‌ی مراحلی که پیش از چاپ باید بدانید.", "۱۲ دقیقه", "۲۰ مرداد ۱۴۰۴"),
    ("layout-2.jpg", "edu", "آموزش", "انتخاب فونت مناسب برای متن کتاب فارسی", "مقایسه‌ی فونت‌های پرکاربرد متن (وزیرمتن، ایران‌سنس، نازنین، لوتوس) بر اساس ژانر اثر.", "۸ دقیقه", "۵ مرداد ۱۴۰۴"),
    ("cover-3.jpg", "kids", "کتاب کودک", "اصول طراحی کتاب کودک: رنگ، فونت و ریتم صفحه", "چرا کتاب کودک با هر کتاب دیگری تفاوت دارد و چگونه کودک را با صفحه همراه کنیم.", "۶ دقیقه", "۱۸ تیر ۱۴۰۴"),
    ("cover-2.jpg", "pub", "راهنمای نشر", "قطع کتاب: رقعی، وزیری یا پالتویی؟", "راهنمای انتخاب قطع استاندارد بر اساس ژانر، تعداد صفحات و بودجه‌ی تولید.", "۴ دقیقه", "۳ تیر ۱۴۰۴"),
]


def blog_cards(limit=None):
    items = BLOG_POSTS if limit is None else BLOG_POSTS[:limit]
    cards = ""
    for i, (img, cat_key, cat_label, title, desc, rt, date) in enumerate(items):
        cards += f"""
      <article class="post reveal" data-cat="{cat_key}" data-delay="{i % 3}">
        <a href="blog.html"><img src="assets/{img}" alt="{title}" loading="lazy"></a>
        <div class="body">
          <span class="cat">{cat_label}</span>
          <h3><a href="blog.html">{title}</a></h3>
          <p>{desc}</p>
          <div class="foot"><span>{date}</span><span>{rt} مطالعه</span></div>
        </div>
      </article>"""
    return cards


BLOG_FILTERS = [("all", "همه"), ("edu", "آموزش"), ("cover", "طراحی جلد"), ("pub", "راهنمای نشر"), ("kids", "کتاب کودک")]


def blog_filter_btns():
    return "".join(
        f'<button type="button" class="filter-btn{" active" if k=="all" else ""}" data-blog-filter="{k}">{v}</button>'
        for k, v in BLOG_FILTERS
    )


# ======================================================
#  صفحه اصلی — پرسونال برندینگ افرا حسین‌زاده
# ======================================================
def index():
    return (
        head(
            "وب‌سایت رسمی",
            "افرا حسین‌زاده — مدیر هنری، طراح جلد کتاب و متخصص صفحه‌آرایی حرفه‌ای با بیش از ۱۰ سال تجربه همکاری با ناشران و نویسندگان",
        )
        + header()
        + f"""
<div class="social-rail" aria-label="شبکه‌های اجتماعی افرا حسین‌زاده">
  <a href="https://instagram.com" target="_blank" rel="noopener" aria-label="اینستاگرام">{ICONS["ig"]}</a>
  <a href="https://t.me" target="_blank" rel="noopener" aria-label="تلگرام">{ICONS["tg"]}</a>
  <a href="https://wa.me/989120000000" target="_blank" rel="noopener" aria-label="واتساپ">{ICONS["wa"]}</a>
  <a href="https://linkedin.com" target="_blank" rel="noopener" aria-label="لینکدین">{ICONS["linkedin"]}</a>
</div>

<!-- سکشن ۱: معرفی و پرتره اصلی افرا حسین‌زاده -->
<section class="pb-hero" id="hero" data-dock-section>
  <div class="hero-watermark" aria-hidden="true">AFRA HOSSEINZADEH</div>
  <div class="container pb-hero-grid">
    <div>
      <div class="pb-role-pill">
        <span class="pulse-dot"></span>
        <span>آماده پذیرش پروژه‌های طراحی جلد و صفحه‌آرایی</span>
      </div>
      <span class="pb-subtitle">افرا حسین‌زاده • مدیر هنری و معمار بصری کتاب</span>
      <h1>هر کتاب ارزشمند، شایسته‌ی <span class="hl">جلدی ماندگار</span> و صفحاتی خوش‌خوان است</h1>
      <p class="lead">بیش از ده سال است که در تقاطع ادبیات، تایپوگرافی فارسی و گرافیک نشر زندگی می‌کنم. به ناشران و نویسندگان مستقل کمک می‌کنم اثرشان با هویتی متمایز، استاندارد چاپی بی‌نقص و خوانایی چشم‌نواز به دست مخاطب برسد.</p>
      <div class="hero-actions">
        <a href="order.html" class="btn btn-primary btn-lg">ثبت سفارش طراحی</a>
        <a href="consult.html" class="btn btn-outline btn-lg">رزرو مشاوره رایگان</a>
        <a href="#portfolio" data-goto-sec="portfolio" class="btn btn-ghost">دیدن نمونه‌کارها {ICONS["arrow"]}</a>
      </div>
      <div class="hero-metrics">
        <div class="h-metric"><b data-count="450" data-prefix="+">۰</b><span>کتاب صفحه‌آرایی‌شده</span></div>
        <div class="h-metric"><b data-count="320" data-prefix="+">۰</b><span>جلد منتشرشده در بازار</span></div>
        <div class="h-metric"><b data-count="98" data-suffix="٪">۰</b><span>رضایت ناشران و مؤلفان</span></div>
      </div>
    </div>

    <div class="portrait-stage">
      <div class="portrait-arch">
        <img class="portrait-img" src="assets/afra-hosseinzadeh.png" width="614" height="820" alt="افرا حسین‌زاده — طراح جلد کتاب و متخصص صفحه‌آرایی" fetchpriority="high">
      </div>
      <div class="portrait-plaque">
        <div>
          <b>افرا حسین‌زاده</b>
          <small>طراح جلد، صفحه‌آرا و مشاور تولید کتاب</small>
        </div>
        <span class="plaque-sign">+۱۰ سال تجربه</span>
      </div>
      <div class="float-card one">
        <span class="ic" style="background:var(--c-teal-light);color:var(--c-teal)">{ICONS["book"]}</span>
        <div><b>+۴۰ ناشر</b><small>همکاری مستمر</small></div>
      </div>
      <div class="float-card two">
        <span class="ic" style="background:var(--c-gold-light);color:var(--c-gold)">{ICONS["clock"]}</span>
        <div><b>۴۸ ساعت</b><small>ارسال اتود اول جلد</small></div>
      </div>
    </div>
  </div>
</section>

<div class="marquee-band" aria-hidden="true">
  <div class="marquee">
    <div class="marquee-track">
      <span><i>✦</i> طراحی جلد اختصاصی کتاب</span>
      <span><i>✦</i> صفحه‌آرایی حرفه‌ای در Adobe InDesign</span>
      <span><i>✦</i> تایپوگرافی و رسم‌الخط معیار فارسی</span>
      <span><i>✦</i> صفحه‌آرایی مجله، سالنامه و کاتالوگ</span>
      <span><i>✦</i> تولید کتاب الکترونیک استاندارد EPUB</span>
      <span><i>✦</i> همکاری با نشر چشمه، نگاه، سمت و مروارید</span>
      <span><i>✦</i> طراحی جلد اختصاصی کتاب</span>
      <span><i>✦</i> صفحه‌آرایی حرفه‌ای در Adobe InDesign</span>
      <span><i>✦</i> تایپوگرافی و رسم‌الخط معیار فارسی</span>
      <span><i>✦</i> صفحه‌آرایی مجله، سالنامه و کاتالوگ</span>
      <span><i>✦</i> تولید کتاب الکترونیک استاندارد EPUB</span>
      <span><i>✦</i> همکاری با نشر چشمه، نگاه، سمت و مروارید</span>
    </div>
  </div>
</div>

<!-- سکشن ۲: اکوسیستم خدمات و مسیرهای همکاری (الهام‌گرفته از Hub در ehsanamirian.com) -->
<section class="section" id="hub" data-dock-section>
  <div class="container">
    <div class="sec-head center">
      <span class="eyebrow">اکوسیستم طراحی افرا</span>
      <h2>مسیرهای همکاری برای خلق یک کتاب استاندارد</h2>
      <p>از ایده‌پردازی اولیه تا خروج کتاب از چاپخانه و انتشار نسخه الکترونیک، تمام بخش‌های تخصصی در یک اکوسیستم یکپارچه گرد هم آمده‌اند.</p>
    </div>

    <div class="bento-grid">
      <a href="#about" data-goto-sec="about" class="bento-card span-8 featured-bio reveal">
        <div class="bio-copy">
          <div class="bento-top">
            <span class="eyebrow" style="margin:0">فلسفه طراحی من</span>
            <span class="bento-go">{ICONS["arrow"]}</span>
          </div>
          <h3 style="font-size:1.35rem;margin-top:.9rem">پیوند میان روح کلمات و معماری بصری صفحه</h3>
          <p>سال‌ها این پرسش دغدغه‌ی من بود: چرا برخی کتاب‌ها به محض باز شدن، خواننده را در آغوش می‌گیرند و برخی دیگر چشم را خسته می‌کنند؟ پاسخ در توازن نامرئی سفیدخوانی، ریتم تایپوگرافی و هویت جلد نهفته است.</p>
        </div>
        <div class="bio-cutout">
          <img src="assets/afra-hosseinzadeh.png" width="614" height="820" alt="افرا حسین‌زاده" loading="lazy">
        </div>
      </a>

      <a href="services.html#cover" class="bento-card reveal" data-delay="1">
        <div class="bento-top">
          <span class="bento-ic">{ICONS["book"]}</span>
          <span class="bento-go">{ICONS["arrow"]}</span>
        </div>
        <div>
          <h3>طراحی جلد کتاب</h3>
          <p>خلق جلدهای مفهومی، تایپوگرافیک و تصویرسازی‌شده برای رمان، شعر، کودک و کتب دانشگاهی.</p>
        </div>
      </a>

      <a href="services.html#layout" class="bento-card reveal">
        <div class="bento-top">
          <span class="bento-ic terra">{ICONS["layout"]}</span>
          <span class="bento-go">{ICONS["arrow"]}</span>
        </div>
        <div>
          <h3>صفحه‌آرایی تخصصی کتاب</h3>
          <p>گریدبندی مهندسی‌شده در ایندیزاین، تنظیم دقیق کشیدگی، نیم‌فاصله، پانویس و نمایه.</p>
        </div>
      </a>

      <a href="services.html#magazine" class="bento-card reveal" data-delay="1">
        <div class="bento-top">
          <span class="bento-ic gold">{ICONS["mag"]}</span>
          <span class="bento-go">{ICONS["arrow"]}</span>
        </div>
        <div>
          <h3>مجله و نشریات ادیتوریال</h3>
          <p>طراحی قالب و مسترپیج اختصاصی برای ماهنامه‌ها، ویژهنامه‌ها و گزارش‌های سالانه سازمانی.</p>
        </div>
      </a>

      <a href="services.html#calc-sec" class="bento-card reveal" data-delay="2">
        <div class="bento-top">
          <span class="bento-ic">{ICONS["layers"]}</span>
          <span class="bento-go">{ICONS["arrow"]}</span>
        </div>
        <div>
          <h3>ماشین‌حساب آنلاین تعرفه</h3>
          <p>برآورد شفاف و لحظه‌ای هزینه طراحی جلد و صفحه‌آرایی بر اساس قطع و تعداد صفحات کتاب.</p>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- سکشن ۳: درباره افرا حسین‌زاده -->
<section class="section section--alt" id="about" data-dock-section>
  <div class="container about-grid">
    <div class="about-img reveal">
      <img src="assets/afra-hosseinzadeh.png" width="614" height="820" alt="افرا حسین‌زاده — طراح جلد و صفحه‌آرا" loading="lazy">
      <div class="exp-badge"><b>۱۰+</b><small>سال سابقه حرفه‌ای</small></div>
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">درباره افرا حسین‌زاده</span>
      <h2>عاشق صفحه‌آرایی‌ام، عاشق کتاب و وسواسی در جزئیات</h2>
      <p>سلام، من <strong>افرا حسین‌زاده</strong> هستم. بیش از یک دهه است که به عنوان طراح جلد و صفحه‌آرا در کنار ناشران باسابقه و مؤلفان مستقل فعالیت می‌کنم. برای من، هر کتاب پیش از آنکه یک پروژه چاپی باشد، حاصل ماه‌ها و سال‌ها اندیشیدن نویسنده است و شایسته است در بهترین قامت بصری دیده شود.</p>
      <p>امروز به همراه تیم تخصصی‌ام در استودیو افرا گرافیک، فرآیند صفحه‌آرایی، طراحی جلد، ویرایش صوری و آماده‌سازی فنی چاپ را به شکلی سیستماتیک و آنلاین برای سراسر ایران و نویسندگان فارسی‌زبان خارج از کشور انجام می‌دهیم.</p>
      <div class="skills">
        <div class="skill" style="--w:98%"><div class="lbl"><span>صفحه‌آرایی حرفه‌ای و گریدبندی (Adobe InDesign)</span><span>۹۸٪</span></div><div class="bar"><i></i></div></div>
        <div class="skill" style="--w:95%"><div class="lbl"><span>طراحی جلد و هویت بصری مجموعه‌های کتاب</span><span>۹۵٪</span></div><div class="bar"><i></i></div></div>
        <div class="skill" style="--w:92%"><div class="lbl"><span>تایپوگرافی فارسی و استانداردهای فنی چاپ (PDF/X)</span><span>۹۲٪</span></div><div class="bar"><i></i></div></div>
      </div>
      <div class="tools"><span>Adobe InDesign</span><span>Photoshop</span><span>Illustrator</span><span>Affinity Publisher</span><span>Figma</span><span>EPUB 3</span></div>
      <div style="margin-top:2rem;display:flex;gap:.8rem;flex-wrap:wrap">
        <a href="about.html" class="btn btn-primary">مطالعه داستان کامل من</a>
        <a href="portfolio.html" class="btn btn-outline">مرور رزومه تصویری</a>
      </div>
    </div>
  </div>
</section>

<!-- سکشن ۴: خدمات و تعرفه‌ها -->
<section class="section" id="services" data-dock-section>
  <div class="container">
    <div class="sec-head center">
      <span class="eyebrow">خدمات تخصصی</span>
      <h2>مسیر اختصاصی کتاب خود را انتخاب کنید</h2>
      <p>تعرفه‌های شفاف، قرارداد مشخص و پشتیبانی کامل فنی تا لحظه تحویل نسخه چاپی از چاپخانه.</p>
    </div>
    <div class="services-grid">
      <article class="service-card reveal">
        <span class="ic">{ICONS["book"]}</span>
        <h3>طراحی جلد کتاب</h3>
        <p>جلدی که در ویترین کتاب‌فروشی و فروشگاه‌های آنلاین نگاه مخاطب را در ۳ ثانیه اول جذب کند.</p>
        <ul>
          <li>۳ اتود اولیه متمایز + ویرایش تا رضایت کامل</li>
          <li>طراحی کامل روی جلد، پشت جلد، عطف و لب‌برگرد</li>
          <li>فایل چاپی CMYK با خط برش + موکاپ سه‌بعدی معرفی</li>
        </ul>
        <div class="price">از ۳٫۵ میلیون تومان <small>/ پروژه</small></div>
        <a href="order.html?service=cover" class="svc-link">ثبت سفارش طراحی جلد {ICONS["arrow"]}</a>
      </article>

      <article class="service-card terra reveal" data-delay="1">
        <span class="ic">{ICONS["layout"]}</span>
        <h3>صفحه‌آرایی کتاب</h3>
        <p>چیدمان استاندارد متن در ایندیزاین با رعایت دقیق اصول خوانایی، حاشیه‌بندی و زیبایی‌شناسی صفحه.</p>
        <ul>
          <li>طراحی یونیفرم، سرفصل‌ها و صفحات آغازین اختصاصی</li>
          <li>چیدمان پانویس، جدول، فرمول، تصویر و نمایه</li>
          <li>خروجی استاندارد چاپخانه + نسخه دیجیتال رایگان</li>
        </ul>
        <div class="price">از ۱۸ هزار تومان <small>/ صفحه</small></div>
        <a href="order.html?service=layout" class="svc-link">ثبت سفارش صفحه‌آرایی {ICONS["arrow"]}</a>
      </article>

      <article class="service-card gold reveal" data-delay="2">
        <span class="ic">{ICONS["mag"]}</span>
        <h3>مجله، کاتالوگ و EPUB</h3>
        <p>طراحی ادیتوریال پویا برای نشریات و تبدیل اصولی کتاب‌های چاپی به فرمت واکنش‌گرای الکترونیک.</p>
        <ul>
          <li>طراحی مسترپیج قابل استفاده برای شماره‌های بعدی</li>
          <li>صفحه‌آرایی اینفوگرافیک‌ها و گزارش‌های عملکرد</li>
          <li>تولید EPUB فارسی سازگار با طاقچه، فیدیبو و کیندل</li>
        </ul>
        <div class="price">از ۴۵ هزار تومان <small>/ صفحه مجله</small></div>
        <a href="services.html" class="svc-link">مشاهده همه تعرفه‌ها و ماشین‌حساب {ICONS["arrow"]}</a>
      </article>
    </div>
  </div>
</section>

<!-- سکشن ۵: نمونه‌کارها -->
<section class="section section--alt" id="portfolio" data-dock-section>
  <div class="container">
    <div class="sec-head center">
      <span class="eyebrow">گزیده آثار افرا حسین‌زاده</span>
      <h2>کتاب‌هایی که با عشق صفحه‌آرایی و طراحی شده‌اند</h2>
      <p>روی هر اثر کلیک کنید تا مشخصات فنی چاپ، ناشر و جزئیات طراحی آن را در نمای بزرگ ببینید.</p>
    </div>
    <div class="filters">{filters()}</div>
    <div class="work-grid">{work_cards()}</div>
    <div class="work-more"><a href="portfolio.html" class="btn btn-outline btn-lg">مشاهده آرشیو کامل نمونه‌کارها</a></div>
  </div>
</section>

<!-- سکشن ۶: فرآیند کار -->
<section class="section" id="process" data-dock-section>
  <div class="container">
    <div class="sec-head center">
      <span class="eyebrow">فرآیند شفاف همکاری</span>
      <h2>در چهار گام دقیق، از فایل خام تا کتاب آماده چاپ</h2>
      <p>بدون سردرگمی و بدون هزینه‌های پنهان؛ در تمام مراحل در جریان پیشرفت پروژه خواهید بود.</p>
    </div>
    <div class="steps">
      <div class="step reveal"><h3>گفت‌وگو و دریافت بریف</h3><p>مشخصات اثر، ژانر، جامعه مخاطب و سلیقه بصری شما را در فرم آنلاین یا جلسه مشاوره بررسی می‌کنیم.</p></div>
      <div class="step reveal" data-delay="1"><h3>اتود جلد و نمونه چیدمان</h3><p>ظرف ۴۸ ساعت اتودهای اولیه جلد یا نمونه صفحه‌آرایی یک فصل از کتاب برای تأیید شما ارسال می‌شود.</p></div>
      <div class="step reveal" data-delay="2"><h3>داوری و اصلاحات دقیق</h3><p>بازخوردهای شما را با حوصله اعمال می‌کنیم تا جزئیات تایپوگرافی و رنگ دقیقاً مطابق خواسته‌تان شود.</p></div>
      <div class="step reveal" data-delay="3"><h3>تحویل فایل چاپ و سورس</h3><p>فایل نهایی PDF/X آماده لیتوگرافی، فایل باز ایندیزاین/فتوشاپ و موکاپ معرفی تحویل داده می‌شود.</p></div>
    </div>
  </div>
</section>

<!-- سکشن ۷: رزرو جلسه مشاوره (الهام‌گرفته از بخش رزرو جلسات ehsanamirian.com) -->
<section class="section section--alt" id="consult" data-dock-section>
  <div class="container">
    <div class="reserve-showcase reveal">
      <div>
        <span class="eyebrow">همراهی پیش از چاپ</span>
        <h2>رزرو جلسه مشاوره رایگان ۲۰ دقیقه‌ای با افرا حسین‌زاده</h2>
        <p>اگر اولین کتاب‌تان را منتشر می‌کنید یا برای انتخاب قطع، نوع کاغذ، صحافی و برآورد هزینه چاپ مردد هستید، شیوه گفت‌وگوی دلخواه‌تان را انتخاب کنید تا زمان جلسه را هماهنگ کنیم.</p>
        <div class="session-modes">
          <div class="mode-card active" data-mode="call">
            {ICONS["phone"]}
            <b>تماس تلفنی</b>
            <small>سریع و مستقیم</small>
          </div>
          <div class="mode-card" data-mode="video">
            {ICONS["video"]}
            <b>جلسه آنلاین تصویری</b>
            <small>بررسی تصویری فایل</small>
          </div>
          <div class="mode-card" data-mode="chat">
            {ICONS["chat"]}
            <b>گفت‌وگو در واتساپ</b>
            <small>تبادل نمونه و ویس</small>
          </div>
        </div>
        <div style="display:flex;gap:.85rem;flex-wrap:wrap">
          <a href="consult.html?mode=call" data-reserve-cta class="btn btn-primary btn-lg">انتخاب روز و ساعت جلسه {ICONS["arrow"]}</a>
          <a href="order.html" class="btn btn-outline btn-lg">مستقیم سفارش می‌دهم</a>
        </div>
      </div>
      <div class="side-card" style="margin:0">
        <h3>در این ۲۰ دقیقه چه مسائلی روشن می‌شود؟</h3>
        <ul class="check-list">
          <li>{ICONS["check"]}<span>انتخاب بهترین قطع و گرید متناسب با حجم و ژانر کتاب</span></li>
          <li>{ICONS["check"]}<span>برآورد دقیق هزینه و زمان طراحی جلد و صفحه‌آرایی</span></li>
          <li>{ICONS["check"]}<span>راهنمایی دریافت شابک، فیپا و مجوز چاپ برای مؤلفان مستقل</span></li>
          <li>{ICONS["check"]}<span>بررسی ایرادهای احتمالی فایل Word پیش از شروع صفحه‌آرایی</span></li>
          <li>{ICONS["check"]}<span>پیشنهاد نوع کاغذ، پوشش جلد (سلفون، طلاکوب، یووی) و صحافی</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- سکشن ۸: نظرات مشتریان + پرسش‌های متداول -->
<section class="section" id="testimonials" data-dock-section>
  <div class="container">
    <div class="sec-head center">
      <span class="eyebrow">دیدگاه ناشران و مؤلفان</span>
      <h2>اعتماد ساخته نمی‌شود؛ از تجربه‌های واقعی شکل می‌گیرد</h2>
    </div>
    <div class="testi-wrap">
      <div class="testi-track">
        <article class="testi">
          <div class="testi-top"><span class="testi-stars">★★★★★</span><span class="testi-rate">(5/5)</span></div>
          <p>صفحه‌آرایی کتاب ۴۰۰ صفحه‌ای ما در کمتر از دو هفته با کیفیتی درخشان تحویل شد. وسواس خانم حسین‌زاده در تراز سطرها و تایپوگرافی فارسی واقعاً کم‌نظیر است.</p>
          <div class="who"><span class="av">م</span><div><b>مریم رضایی</b><small>مدیر تولید نشر نگاه</small></div></div>
        </article>
        <article class="testi">
          <div class="testi-top"><span class="testi-stars">★★★★★</span><span class="testi-rate">(5/5)</span></div>
          <p>اولین کتابم بود و هیچ تجربه‌ای از فرآیند چاپ نداشتم. جلسه‌ی مشاوره رایگان همه‌چیز را شفاف کرد و جلد نهایی دقیقاً روح داستانم را بازتاب می‌دهد.</p>
          <div class="who"><span class="av" style="background:var(--c-terra)">ع</span><div><b>علی محمدی</b><small>نویسنده‌ی مستقل</small></div></div>
        </article>
        <article class="testi">
          <div class="testi-top"><span class="testi-stars">★★★★★</span><span class="testi-rate">(5/5)</span></div>
          <p>برای ماهنامه‌مان مسترپیج و هویت ادیتوریال جدیدی طراحی شد که هم فوق‌العاده چشم‌نواز است و هم زمان بستن هر شماره را به نصف کاهش داده است.</p>
          <div class="who"><span class="av" style="background:var(--c-gold)">س</span><div><b>سارا کریمی</b><small>سردبیر ماهنامه هنر و اندیشه</small></div></div>
        </article>
        <article class="testi">
          <div class="testi-top"><span class="testi-stars">★★★★★</span><span class="testi-rate">(5/5)</span></div>
          <p>سه نوبت چاپ از کتاب دانشگاهی ما با صفحه‌آرایی افرا منتشر شده و خوانایی جداول و نمودارها همیشه مورد تحسین دانشجویان و همکاران بوده است.</p>
          <div class="who"><span class="av" style="background:var(--c-ink-2)">د</span><div><b>دکتر حمید احمدی</b><small>عضو هیئت علمی دانشگاه</small></div></div>
        </article>
      </div>
      <div class="testi-ctrl">
        <button type="button" class="icon-btn" data-testi="prev" aria-label="قبلی">{ICONS["arrow_r"]}</button>
        <button type="button" class="icon-btn" data-testi="next" aria-label="بعدی">{ICONS["arrow"]}</button>
      </div>
    </div>

    <div style="margin-top:4rem">
      <div class="sec-head center"><span class="eyebrow">پرسش‌های پرتکرار</span><h2>پاسخ به دغدغه‌های رایج پیش از ثبت سفارش</h2></div>
      <div class="faq">
        <details><summary>هزینه‌ی طراحی جلد و صفحه‌آرایی چطور محاسبه می‌شود؟</summary><div class="ans">هزینه‌ی صفحه‌آرایی بر اساس تعداد صفحه، ساختار متن (ساده، پانویس‌دار، جدول و فرمول یا مصور) و زمان تحویل محاسبه می‌شود. طراحی جلد تعرفه پایه مشخص دارد. در <a href="services.html#calc-sec" style="color:var(--c-teal);font-weight:700">ماشین‌حساب صفحه تعرفه‌ها</a> می‌توانید به صورت آنی هزینه را محاسبه کنید.</div></details>
        <details><summary>زمان تحویل پروژه چقدر است؟</summary><div class="ans">اتود اولیه‌ی جلد ظرف ۴۸ ساعت کاری ارسال می‌شود. صفحه‌آرایی یک کتاب ۲۰۰ صفحه‌ای متنی به طور میانگین ۵ تا ۷ روز کاری زمان می‌برد و امکان سفارش فوری نیز فراهم است.</div></details>
        <details><summary>چند بار امکان ویرایش و اصلاح طرح وجود دارد؟</summary><div class="ans">در چارچوب بریف توافق‌شده، اصلاحات تا جلب رضایت کامل شما بدون هزینه اضافه انجام می‌گیرد.</div></details>
        <details><summary>در پایان پروژه چه فایل‌هایی تحویل می‌گیرم؟</summary><div class="ans">فایل PDF/X آماده چاپخانه با رنگ CMYK و خط برش، فایل باز لایه‌باز (InDesign / Photoshop)، نسخه دیجیتال معرفی و موکاپ سه‌بعدی جلد.</div></details>
      </div>
    </div>
  </div>
</section>

<!-- سکشن ۹: مجله تخصصی -->
<section class="section section--alt" id="blog" data-dock-section>
  <div class="container">
    <div class="sec-head center">
      <span class="eyebrow">مجله و یادداشت‌ها</span>
      <h2>یادداشت‌های تخصصی افرا درباره طراحی کتاب و نشر</h2>
      <p>تجربه‌های عملی از دنیای تایپوگرافی فارسی، روان‌شناسی جلد و مسیر چاپ کتاب.</p>
    </div>
    <div class="filters">{blog_filter_btns()}</div>
    <div class="blog-grid">{blog_cards(3)}</div>
    <div class="work-more"><a href="blog.html" class="btn btn-outline btn-lg">مطالعه همه مقالات مجله</a></div>
  </div>
</section>

<!-- سکشن ۱۰: ارتباط مستقیم با افرا -->
<section class="section" id="contact" data-dock-section>
  <div class="container">
    <div class="sec-head center">
      <span class="eyebrow">ارتباط مستقیم</span>
      <h2>گفت‌وگو درباره کتاب بعدی شما</h2>
      <p>از هر راهی که برای‌تان راحت‌تر است پیام بگذارید؛ معمولاً در کمتر از چند ساعت کاری پاسخ‌گو هستم.</p>
    </div>
    <div class="contact-cards">
      <a href="tel:+989120000000" class="ccard reveal"><span class="ic">{ICONS["phone"]}</span><b>تماس مستقیم و واتساپ</b><span>0912 000 0000</span></a>
      <a href="mailto:info@afradesigner.ir" class="ccard reveal" data-delay="1"><span class="ic" style="background:var(--c-terra-light);color:var(--c-terra)">{ICONS["mail"]}</span><b>پست الکترونیک</b><span>info@afradesigner.ir</span></a>
      <a href="consult.html" class="ccard reveal" data-delay="2"><span class="ic" style="background:var(--c-gold-light);color:var(--c-gold)">{ICONS["calendar"]}</span><b>نوبت مشاوره آنلاین</b><span style="direction:rtl">رزرو رایگان در تقویم شمسی</span></a>
    </div>
    <div class="two-col" style="grid-template-columns:1.2fr .8fr">
      <form class="form-card" data-simple="پیام شما برای افرا حسین‌زاده ارسال شد ✅" novalidate>
        <h3>ارسال پیام سریع</h3>
        <div class="form-grid" style="margin-top:1rem">
          <div class="field"><label>نام شما <span class="req">*</span></label><input name="name" required placeholder="نام و نام خانوادگی"><div class="err">نام را وارد کنید</div></div>
          <div class="field"><label>شماره موبایل <span class="req">*</span></label><input name="phone" type="tel" required placeholder="0912..." style="direction:ltr;text-align:right"><div class="err">شماره معتبر وارد کنید</div></div>
          <div class="field full"><label>پیام یا توضیح کوتاه درباره کتاب <span class="req">*</span></label><textarea name="message" required placeholder="عنوان یا ژانر کتاب، تعداد صفحات تقریبی و سوال شما…"></textarea><div class="err">متن پیام را بنویسید</div></div>
        </div>
        <div style="margin-top:1.25rem"><button type="submit" class="btn btn-primary btn-lg">ارسال پیام</button></div>
      </form>
      <div class="cta" style="text-align:right;padding:2.2rem;display:flex;flex-direction:column;justify-content:center">
        <h3 style="color:#fff;font-size:1.45rem">پروژه‌ی آماده سفارش دارید؟</h3>
        <p style="margin:0 0 1.5rem">با تکمیل فرم ۴ مرحله‌ای سفارش، برآورد آنی هزینه را ببینید و کد پیگیری اختصاصی دریافت کنید.</p>
        <a href="order.html" class="btn btn-primary btn-lg" style="align-self:flex-start">ورود به فرم ثبت سفارش {ICONS["arrow"]}</a>
      </div>
    </div>
  </div>
</section>
"""
        + footer(is_home=True)
    )


# ======================================================
#  خدمات و تعرفه
# ======================================================
def services():
    def svc(id_, icon, cls, title, desc, items, price, svc_q="both"):
        return f"""
    <article class="service-card {cls} reveal" id="{id_}">
      <span class="ic">{ICONS[icon]}</span>
      <h3>{title}</h3>
      <p>{desc}</p>
      <ul>{"".join(f"<li>{i}</li>" for i in items)}</ul>
      <div class="price">{price}</div>
      <div style="margin-top:1.2rem"><a href="order.html?service={svc_q}" class="btn btn-sm btn-primary">سفارش این خدمت</a></div>
    </article>"""

    return (
        head(
            "خدمات و تعرفه",
            "لیست کامل خدمات طراحی جلد، صفحه‌آرایی کتاب و مجله، کتاب الکترونیک و آماده‌سازی چاپ توسط افرا حسین‌زاده به همراه ماشین‌حساب تعرفه",
        )
        + header()
        + page_hero(
            "خدمات و تعرفه",
            "خدمات تخصصی و تعرفه‌ها",
            "تمام قیمت‌ها شفاف و بدون هزینه‌ی پنهان است. برآورد نهایی پس از بررسی نمونه فایل شما اعلام می‌شود.",
        )
        + f"""
<section class="section--tight">
  <div class="container services-grid">
    {svc("cover", "book", "", "طراحی جلد کتاب", "طراحی اختصاصی جلد متناسب با ژانر، مخاطب و هویت ناشر؛ شامل روی جلد، پشت جلد و عطف.", ["۳ اتود اولیه با رویکردهای متفاوت", "ویرایش نامحدود تا رضایت کامل", "طراحی عطف با محاسبه‌ی دقیق ضخامت کاغذ", "فایل چاپ CMYK با خط برش و لب‌برگرد", "نسخه‌ی موکاپ سه‌بعدی برای معرفی"], "از ۳٫۵ میلیون تومان <small>/ پروژه</small>", "cover")}
    {svc("layout", "layout", "terra", "صفحه‌آرایی کتاب", "چیدمان حرفه‌ای متن در Adobe InDesign با رعایت اصول تایپوگرافی فارسی و استانداردهای چاپ.", ["انتخاب فونت، اندازه و گرید اختصاصی", "طراحی صفحات آغازین، فهرست و شناسنامه", "پانویس، نمایه، جدول و تصویر", "نمونه‌خوانی چیدمان پیش از تحویل", "خروجی PDF چاپ + نسخه‌ی دیجیتال"], "از ۱۸ هزار تومان <small>/ صفحه</small>", "layout")}
    {svc("magazine", "mag", "gold", "صفحه‌آرایی مجله و کاتالوگ", "طراحی ادیتوریال پویا برای مجلات، کاتالوگ محصولات و گزارش‌های سالانه.", ["طراحی تمپلیت و مسترپیج قابل استفاده‌ی مجدد", "گرید چندستونه، نقل‌قول و اینفوگرافیک", "رتوش و آماده‌سازی تصاویر", "هماهنگی فنی با چاپخانه"], "از ۴۵ هزار تومان <small>/ صفحه</small>", "magazine")}
    {svc("ebook", "tablet", "", "کتاب الکترونیک (EPUB / PDF)", "تبدیل کتاب به نسخه‌ی دیجیتال استاندارد برای طاقچه، فیدیبو و کیندل.", ["EPUB واکنش‌گرا با پشتیبانی کامل فارسی", "PDF تعاملی با فهرست کلیک‌شونده", "بهینه‌سازی حجم تصاویر", "تست نمایش روی دستگاه‌های مختلف"], "از ۱۲ هزار تومان <small>/ صفحه</small>", "ebook")}
    {svc("edit", "edit", "terra", "ویراستاری و نمونه‌خوانی", "ویرایش صوری و فنی متن پیش از صفحه‌آرایی برای متنی پاکیزه و یک‌دست.", ["اصلاح رسم‌الخط و نشانه‌گذاری", "یک‌دست‌سازی نیم‌فاصله و اعداد فارسی", "بررسی ارجاعات و پانویس‌ها"], "از ۶ هزار تومان <small>/ صفحه</small>", "layout")}
    {svc("print", "print", "gold", "آماده‌سازی و نظارت چاپ", "بررسی فنی فایل، پروف رنگی و همراهی تا خروج کتاب از چاپخانه.", ["Preflight فنی فایل نهایی", "مشاوره‌ی انتخاب کاغذ و پوشش جلد", "معرفی چاپخانه‌های معتبر همکار", "بررسی نمونه‌ی چاپی (پروف)"], "توافقی <small>/ بسته به تیراژ</small>", "both")}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head center"><span class="eyebrow">بسته‌های پیشنهادی</span><h2>بسته‌ای متناسب با کتاب‌تان انتخاب کنید</h2><p>برای کتاب‌های متنی تا ۲۰۰ صفحه. برای پروژه‌های بزرگ‌تر، قیمت اختصاصی اعلام می‌شود.</p></div>
    <div class="pricing">
      <div class="plan reveal">
        <h3>پایه</h3>
        <div class="p">۴٫۹ <small>میلیون تومان</small></div>
        <p class="desc">مناسب نویسندگان مستقل با بودجه‌ی اقتصادی</p>
        <ul><li>صفحه‌آرایی تا ۲۰۰ صفحه‌ی متنی</li><li>طراحی جلد (۲ اتود)</li><li>۲ دور اصلاح</li><li>فایل چاپ PDF</li><li class="no">فایل باز ایندیزاین</li><li class="no">نسخه‌ی EPUB</li></ul>
        <a href="order.html?service=both&pages=200" class="btn btn-outline btn-block">انتخاب بسته پایه</a>
      </div>
      <div class="plan featured reveal" data-delay="1">
        <span class="badge">محبوب‌ترین</span>
        <h3>حرفه‌ای</h3>
        <div class="p">۷٫۹ <small>میلیون تومان</small></div>
        <p class="desc">انتخاب اول ناشران و مؤلفان دغدغه‌مند</p>
        <ul><li>صفحه‌آرایی تا ۲۰۰ صفحه (با جدول و تصویر)</li><li>طراحی جلد (۳ اتود) + عطف و پشت جلد</li><li>اصلاح نامحدود تا رضایت کامل</li><li>فایل چاپ + فایل باز لایه‌باز</li><li>نسخه‌ی EPUB استاندارد</li><li>موکاپ سه‌بعدی برای معرفی</li></ul>
        <a href="order.html?service=both&pages=200" class="btn btn-primary btn-block">انتخاب بسته حرفه‌ای</a>
      </div>
      <div class="plan reveal" data-delay="2">
        <h3>همکاری ناشران</h3>
        <div class="p">توافقی</div>
        <p class="desc">قرارداد دوره‌ای برای مجموعه‌ی عناوین انتشارات</p>
        <ul><li>تخفیف پلکانی بر اساس تعداد عنوان</li><li>طراحی هویت بصری یکپارچه مجموعه (یونیفرم)</li><li>اولویت در زمان‌بندی تولید</li><li>ارتباط مستقیم با افرا حسین‌زاده</li><li>نظارت فنی چاپ</li><li>گزارش ماهانه پروژه‌ها</li></ul>
        <a href="consult.html" class="btn btn-outline btn-block">درخواست جلسه هماهنگی</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" id="calc-sec">
  <div class="container two-col">
    <div>
      <span class="eyebrow">ماشین‌حساب هوشمند</span>
      <h2>برآورد سریع هزینه طراحی</h2>
      <p>مشخصات کتاب‌تان را تغییر دهید تا برآورد تقریبی را همان لحظه ببینید و با یک کلیک وارد فرم سفارش شوید.</p>
      <form id="calc" class="form-card" style="box-shadow:none">
        <div class="form-grid">
          <div class="field">
            <label>نوع اثر</label>
            <select name="type"><option value="book">کتاب متنی (رمان، داستان، شعر)</option><option value="academic">کتاب دانشگاهی / پژوهشی</option><option value="kids">کتاب کودک (مصور)</option><option value="magazine">مجله / کاتالوگ</option><option value="ebook">فقط کتاب الکترونیک</option></select>
          </div>
          <div class="field">
            <label>تعداد صفحات</label>
            <input type="number" name="pages" min="1" value="200">
          </div>
          <div class="field full" style="display:flex;gap:1.5rem;flex-wrap:wrap">
            <label style="display:flex;align-items:center;gap:.5rem;font-weight:600;cursor:pointer"><input type="checkbox" name="cover" checked style="width:18px;height:18px;accent-color:var(--c-teal)"> طراحی جلد هم می‌خواهم</label>
            <label style="display:flex;align-items:center;gap:.5rem;font-weight:600;cursor:pointer"><input type="checkbox" name="edit" style="width:18px;height:18px;accent-color:var(--c-teal)"> نمونه‌خوانی و ویرایش صوری</label>
          </div>
        </div>
        <div class="estimate"><div><small>برآورد تقریبی</small><b id="calc-out">—</b></div><a href="order.html?service=both&pages=200" data-calc-order class="btn btn-primary">ثبت سفارش با این مشخصات</a></div>
      </form>
    </div>
    <aside class="sticky">
      <div class="side-card">
        <h3>در همه‌ی خدمات تضمین می‌شود</h3>
        <ul class="check-list">
          <li>{ICONS["check"]}<span>جلسه‌ی مشاوره‌ی رایگان اولیه با افرا</span></li>
          <li>{ICONS["check"]}<span>قرارداد شفاف و زمان‌بندی دقیق تحویل</span></li>
          <li>{ICONS["check"]}<span>ارسال پیش‌نمایش پیش از تسویه نهایی</span></li>
          <li>{ICONS["check"]}<span>پشتیبانی فنی ۳۰ روزه تا پایان چاپ</span></li>
          <li>{ICONS["check"]}<span>حفظ کامل محرمانگی و حقوق مادی و معنوی اثر</span></li>
        </ul>
      </div>
      <div class="side-card" style="background:linear-gradient(135deg,#0b3c2d,#136f53);color:#fff;border:0">
        <h3 style="color:#fff">مطمئن نیستید کدام بسته مناسب شماست؟</h3>
        <p style="color:rgba(255,255,255,.82);font-size:.92rem">در یک گفت‌وگوی ۲۰ دقیقه‌ای رایگان بهترین مسیر را با هم انتخاب می‌کنیم.</p>
        <a href="consult.html" class="btn btn-block" style="background:#fff;color:#0b3c2d">رزرو مشاوره رایگان</a>
      </div>
    </aside>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head center"><span class="eyebrow">جدول جزئیات</span><h2>مقایسه‌ی تعرفه‌ی صفحه‌آرایی بر اساس نوع متن</h2></div>
    <div class="table-wrap">
      <table class="table">
        <thead><tr><th>نوع محتوا</th><th>قیمت هر صفحه</th><th>زمان تقریبی (۲۰۰ صفحه)</th><th>توضیح</th></tr></thead>
        <tbody>
          <tr><td>متن ساده (رمان، داستان، خاطرات)</td><td>۱۸٬۰۰۰ تومان</td><td>۵ روز کاری</td><td>بدون جدول و تصویر</td></tr>
          <tr><td>متن با پانویس و ارجاع</td><td>۲۲٬۰۰۰ تومان</td><td>۷ روز کاری</td><td>کتب دانشگاهی و علوم انسانی</td></tr>
          <tr><td>متن با جدول، فرمول و نمودار</td><td>۲۸٬۰۰۰ تومان</td><td>۱۰ روز کاری</td><td>کتب فنی، مهندسی و پزشکی</td></tr>
          <tr><td>شعر (کلاسیک و نو)</td><td>۱۵٬۰۰۰ تومان</td><td>۴ روز کاری</td><td>چیدمان دقیق مصرع و بیت</td></tr>
          <tr><td>کتاب کودک مصور</td><td>۶۰٬۰۰۰ تومان</td><td>۱۰ روز کاری</td><td>ترکیب تصویرسازی و لترینگ</td></tr>
          <tr><td>مجله / کاتالوگ ادیتوریال</td><td>۴۵٬۰۰۰ تومان</td><td>۷ روز کاری</td><td>گرید چندستونه و گرافیک خبری</td></tr>
        </tbody>
      </table>
    </div>
    <p class="muted text-center" style="margin-top:1rem;font-size:.85rem">* تحویل سریع (نصف زمان معمول) با ۳۰٪ افزایش تعرفه و تحویل خیلی فوری با ۶۰٪ افزایش تعرفه انجام می‌شود.</p>
  </div>
</section>
{cta_block()}
"""
        + footer()
    )


# ======================================================
#  نمونه‌کارها
# ======================================================
def portfolio():
    extra = WORKS + [
        ("cover-2.jpg", "cover", "طراحی جلد", "مجموعه شعر «سایه‌ی سرو»", "بازطراحی جلد برای چاپ ششم با حفظ هویت نسخه‌ی اصلی", "نشر ثالث | شومیز | رقعی", False),
        ("layout-1.jpg", "academic", "دانشگاهی", "مبانی اقتصاد خرد", "صفحه‌آرایی ۵۲۰ صفحه با ۱۴۰ جدول و نمودار برداری", "انتشارات سمت | وزیری | ۱۴۰۳", False),
        ("cover-1.jpg", "cover", "طراحی جلد", "رمان «باران در آبان»", "جلد مینیمال با بافت کاغذ کتان و طلاکوب گرم", "نشر افق | جلد سخت | رقعی", False),
    ]
    cards = ""
    for i, (img, cat, cat_label, title, desc, meta, wide) in enumerate(extra):
        cards += f"""
      <article class="work reveal{" wide" if wide else ""}" data-cat="{cat}" data-cat-label="{cat_label}" data-title="{title}" data-desc="{desc}" data-meta="{meta}" data-delay="{i % 3}">
        <img src="assets/{img}" alt="{title}" loading="lazy">
        <div class="work-info"><span class="tag">{cat_label}</span><h3>{title}</h3><p>{meta.split('|')[0].strip()}</p></div>
      </article>"""
    return (
        head("نمونه‌کارها", "گالری نمونه‌کارهای طراحی جلد و صفحه‌آرایی کتاب، مجله و کتاب کودک اثر افرا حسین‌زاده")
        + header()
        + page_hero("نمونه‌کارها", "آرشیو نمونه‌کارهای افرا حسین‌زاده", "گزیده‌ای از بیش از ۷۰۰ پروژه‌ی طراحی جلد و صفحه‌آرایی منتشرشده. برای دیدن شناسنامه‌ی هر اثر روی آن کلیک کنید.")
        + f"""
<section class="section--tight">
  <div class="container">
    <div class="filters">{filters()}</div>
    <div class="work-grid">{cards}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid-3">
      <div class="card reveal text-center"><span class="ic" style="display:inline-grid;place-items:center;width:56px;height:56px;border-radius:16px;background:var(--c-teal-light);color:var(--c-teal);margin-bottom:1rem">{ICONS["book"]}</span><h3>+۳۲۰ جلد کتاب</h3><p class="muted">در ژانرهای ادبی، کودک، دانشگاهی و عمومی</p></div>
      <div class="card reveal text-center" data-delay="1"><span class="ic" style="display:inline-grid;place-items:center;width:56px;height:56px;border-radius:16px;background:var(--c-terra-light);color:var(--c-terra);margin-bottom:1rem">{ICONS["layout"]}</span><h3>+۹۰٬۰۰۰ صفحه</h3><p class="muted">صفحه‌آرایی استاندارد در Adobe InDesign</p></div>
      <div class="card reveal text-center" data-delay="2"><span class="ic" style="display:inline-grid;place-items:center;width:56px;height:56px;border-radius:16px;background:var(--c-gold-light);color:var(--c-gold);margin-bottom:1rem">{ICONS["users"]}</span><h3>+۴۰ ناشر معتبر</h3><p class="muted">همکاری مستمر با انتشارات برتر کشور</p></div>
    </div>
  </div>
</section>
{cta_block()}
"""
        + footer()
    )


# ======================================================
#  ثبت سفارش
# ======================================================
def order():
    def choice(val, icon, title, sub, checked=False):
        return f"""<label class="choice"><input type="radio" name="service" value="{val}" {"checked" if checked else ""}><span class="box">{ICONS[icon]}<b>{title}</b><small>{sub}</small></span></label>"""

    return (
        head("ثبت سفارش آنلاین", "ثبت آنلاین سفارش طراحی جلد و صفحه‌آرایی کتاب با افرا حسین‌زاده در ۴ مرحله ساده با برآورد آنی هزینه")
        + header()
        + page_hero("ثبت سفارش", "ثبت سفارش آنلاین پروژه", "در ۴ مرحله‌ی کوتاه مشخصات کتاب یا نشریه خود را ثبت کنید. برآورد اولیه همان لحظه نمایش داده می‌شود و ظرف ۲۴ ساعت با شما تماس می‌گیریم.")
        + f"""
<section class="section--tight">
  <div class="container two-col">
    <div id="order-wrap">
      <form id="order-form" class="form-card" novalidate>
        <div class="stepper">
          <div class="s active"><i></i><span>نوع خدمت</span></div>
          <div class="s"><i></i><span>مشخصات اثر</span></div>
          <div class="s"><i></i><span>اطلاعات تماس</span></div>
          <div class="s"><i></i><span>بازبینی</span></div>
        </div>

        <!-- مرحله ۱ -->
        <div class="step-pane active">
          <h3>چه خدمتی نیاز دارید؟</h3>
          <p class="muted">می‌توانید جزئیات را بعداً در گفت‌وگوی تلفنی نیز تغییر دهید.</p>
          <div class="field" data-required-group>
            <div class="choice-grid">
              {choice("cover", "book", "طراحی جلد", "روی جلد، پشت جلد و عطف")}
              {choice("layout", "layout", "صفحه‌آرایی", "چیدمان صفحات داخلی", True)}
              {choice("both", "shield", "جلد + صفحه‌آرایی", "بسته‌ی کامل با تخفیف")}
              {choice("magazine", "mag", "مجله / کاتالوگ", "طراحی ادیتوریال")}
              {choice("ebook", "tablet", "کتاب الکترونیک", "EPUB / PDF تعاملی")}
            </div>
            <div class="err">لطفاً یک خدمت انتخاب کنید</div>
          </div>
          <div class="form-grid" style="margin-top:1.5rem">
            <div class="field">
              <label for="urgency">زمان تحویل <span class="req">*</span></label>
              <select id="urgency" name="urgency" required>
                <option value="normal">عادی (زمان استاندارد)</option>
                <option value="fast">سریع (۳۰٪ افزایش قیمت)</option>
                <option value="urgent">خیلی فوری (۶۰٪ افزایش قیمت)</option>
              </select>
            </div>
            <div class="field">
              <label for="pages">تعداد صفحات تقریبی <span class="opt">(برای صفحه‌آرایی)</span></label>
              <input type="number" id="pages" name="pages" min="0" placeholder="مثلاً ۲۰۰" value="200">
            </div>
          </div>
          <div class="estimate"><div><small>برآورد اولیه‌ی هزینه</small><b id="estimate">—</b></div><small style="max-width:260px">این عدد تقریبی است و قیمت نهایی پس از بررسی نمونه فایل اعلام می‌شود.</small></div>
        </div>

        <!-- مرحله ۲ -->
        <div class="step-pane">
          <h3>مشخصات اثر</h3>
          <p class="muted">هرچه اطلاعات دقیق‌تر باشد، اتودهای اولیه به سلیقه‌ی شما نزدیک‌تر خواهد بود.</p>
          <div class="form-grid">
            <div class="field full"><label for="title">عنوان کتاب / نشریه <span class="req">*</span></label><input id="title" name="title" required placeholder="مثلاً: برگ‌های ارغوانی"><div class="err">عنوان اثر را وارد کنید</div></div>
            <div class="field">
              <label for="genre">ژانر / موضوع <span class="req">*</span></label>
              <select id="genre" name="genre" required>
                <option value="">انتخاب کنید…</option><option>رمان و داستان</option><option>شعر</option><option>کودک و نوجوان</option><option>دانشگاهی و علمی</option><option>روان‌شناسی و توسعه فردی</option><option>تاریخ و علوم انسانی</option><option>مجله و نشریه</option><option>سایر</option>
              </select><div class="err">ژانر را انتخاب کنید</div>
            </div>
            <div class="field">
              <label for="size">قطع کتاب</label>
              <select id="size" name="size"><option>رقعی (۱۴٫۵×۲۱٫۵)</option><option>وزیری (۱۷×۲۴)</option><option>رحلی (۲۱×۲۸)</option><option>خشتی (۲۱×۲۱)</option><option>پالتویی (۱۲×۲۱)</option><option>جیبی (۱۱×۱۷)</option><option>A4</option><option>سایر / نیاز به مشورت دارم</option></select>
            </div>
            <div class="field"><label for="author">نام نویسنده / ناشر</label><input id="author" name="author" placeholder="اختیاری"></div>
            <div class="field">
              <label for="binding">نوع جلد</label>
              <select id="binding" name="binding"><option>شومیز (نرم)</option><option>سخت (گالینگور)</option><option>سخت با روکش</option><option>نمی‌دانم — مشاوره می‌خواهم</option></select>
            </div>
            <div class="field full"><label for="brief">توضیحات و سلیقه‌ی بصری شما</label><textarea id="brief" name="brief" placeholder="خلاصه‌ی اثر، حال‌وهوای مورد نظر، رنگ‌های محبوب، نمونه‌های الهام‌بخش…"></textarea></div>
            <div class="field full">
              <label>فایل‌های پیوست <span class="opt">(اختیاری — نمونه متن، تصاویر یا طرح‌های مرجع)</span></label>
              <div class="upload">{ICONS["upload"]}<b>فایل را این‌جا رها کنید یا کلیک نمایید</b><p class="muted" style="margin:.3rem 0 0;font-size:.85rem">Word، PDF، تصویر — حداکثر ۵۰ مگابایت</p><input type="file" multiple></div>
              <ul class="upload-list"></ul>
            </div>
          </div>
        </div>

        <!-- مرحله ۳ -->
        <div class="step-pane">
          <h3>اطلاعات تماس</h3>
          <p class="muted">برای هماهنگی و ارسال پیش‌نمایش طرح‌ها از این اطلاعات استفاده می‌کنیم.</p>
          <div class="form-grid">
            <div class="field"><label for="name">نام و نام خانوادگی <span class="req">*</span></label><input id="name" name="name" required placeholder="نام شما"><div class="err">نام را وارد کنید</div></div>
            <div class="field"><label for="phone">شماره موبایل <span class="req">*</span></label><input id="phone" name="phone" type="tel" required placeholder="09xx xxx xxxx" style="direction:ltr;text-align:right"><div class="err">شماره موبایل معتبر وارد کنید</div></div>
            <div class="field"><label for="email">ایمیل <span class="opt">(اختیاری)</span></label><input id="email" name="email" type="email" placeholder="you@example.com" style="direction:ltr;text-align:right"><div class="err">ایمیل معتبر وارد کنید</div></div>
            <div class="field">
              <label for="contactvia">روش ارتباط ترجیحی</label>
              <select id="contactvia" name="contactvia"><option>تماس تلفنی</option><option>واتساپ</option><option>تلگرام</option><option>ایمیل</option></select>
            </div>
            <div class="field full">
              <label for="role">معرفی کوتاه</label>
              <select id="role" name="role"><option>نویسنده‌ی مستقل هستم</option><option>نماینده انتشارات هستم</option><option>مترجم هستم</option><option>سازمان / شرکت هستم</option></select>
            </div>
          </div>
        </div>

        <!-- مرحله ۴ -->
        <div class="step-pane">
          <h3>بازبینی و ثبت نهایی</h3>
          <p class="muted">لطفاً خلاصه‌ی سفارش خود را بررسی کنید. پس از ارسال، کد رهگیری اختصاصی صادر می‌شود.</p>
          <div class="summary"><dl id="summary"></dl></div>
          <div class="field" style="margin-top:1.25rem">
            <label style="display:flex;gap:.6rem;align-items:flex-start;font-weight:500;font-size:.92rem;cursor:pointer"><input type="checkbox" name="agree" required style="width:18px;height:18px;margin-top:.3rem;accent-color:var(--c-teal)"><span>قوانین همکاری و حفظ محرمانگی فایل‌ها را مطالعه کرده‌ام و می‌پذیرم.</span></label>
            <div class="err">برای ثبت نهایی، پذیرش شرایط همکاری الزامی است</div>
          </div>
        </div>

        <div class="step-nav">
          <button type="button" class="btn btn-outline hidden" data-prev>مرحله قبل</button>
          <span></span>
          <button type="button" class="btn btn-primary" data-next>مرحله بعد</button>
          <button type="submit" class="btn btn-accent hidden" data-submit>ثبت نهایی سفارش</button>
        </div>
      </form>
    </div>

    <div id="order-success" class="form-card success hidden">
      <div class="ok">{ICONS["check"]}</div>
      <h2>سفارش شما با موفقیت ثبت شد 🎉</h2>
      <p>سپاس از اعتماد شما به افرا حسین‌زاده. کد رهگیری پروژه:</p>
      <div class="code">AF-000000</div>
      <p class="muted">حداکثر تا ۲۴ ساعت کاری آینده برای هماهنگی جزئیات و اعلام زمان‌بندی دقیق با شما تماس می‌گیریم.</p>
      <div style="display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap;margin-top:1.5rem">
        <a href="index.html" class="btn btn-outline">بازگشت به صفحه اصلی</a>
        <a href="consult.html" class="btn btn-primary">رزرو جلسه‌ی مشاوره</a>
      </div>
    </div>

    <aside class="sticky">
      <div class="side-card">
        <h3>مراحل پس از ثبت سفارش</h3>
        <ul class="timeline">
          <li><small>گام اول — تا ۲۴ ساعت</small><b>تماس هماهنگی</b><p>بررسی فایل نمونه و اعلام زمان‌بندی و قیمت قطعی.</p></li>
          <li><small>گام دوم</small><b>قرارداد و شروع پروژه</b><p>۴۰٪ پیش‌پرداخت و آغاز طراحی اتودها.</p></li>
          <li><small>گام سوم — ۴۸ ساعت بعد</small><b>ارسال اتود اولیه</b><p>مشاهده طرح جلد یا نمونه صفحات چیدمان‌شده.</p></li>
          <li><small>گام پایانی</small><b>تحویل پکیج کامل</b><p>فایل چاپ PDF/X، سورس باز و نسخه دیجیتال.</p></li>
        </ul>
      </div>
      <div class="side-card">
        <h3>نیاز به راهنمایی پیش از سفارش دارید؟</h3>
        <p style="font-size:.92rem">می‌توانید همین حالا جلسه مشاوره رایگان رزرو کنید یا در واتساپ پیام بگذارید:</p>
        <a href="consult.html" class="btn btn-outline btn-block" style="margin-bottom:.6rem">رزرو مشاوره رایگان</a>
        <a href="https://wa.me/989120000000" target="_blank" rel="noopener" class="btn btn-block" style="background:#25d366;color:#fff">{ICONS["wa"]} گفتگو در واتساپ</a>
      </div>
    </aside>
  </div>
</section>
"""
        + footer()
    )


# ======================================================
#  مشاوره
# ======================================================
def consult():
    return (
        head("مشاوره رایگان", "رزرو آنلاین جلسه مشاوره رایگان ۲۰ دقیقه‌ای طراحی جلد و صفحه‌آرایی کتاب با افرا حسین‌زاده")
        + header()
        + page_hero("مشاوره رایگان", "رزرو مشاوره‌ی رایگان با افرا حسین‌زاده", "۲۰ دقیقه گفت‌وگوی تخصصی درباره‌ی کتاب، انتخاب قطع، مسیر چاپ و برآورد شفاف هزینه — بدون هیچ پیش‌شرطی.")
        + f"""
<section class="section--tight">
  <div class="container two-col">
    <div id="consult-wrap">
      <form id="consult-form" class="form-card" novalidate>
        <h3>۱. انتخاب روز و ساعت (تقویم شمسی)</h3>
        <p class="muted" style="font-size:.9rem">ساعات به وقت تهران است. روزهای جمعه تعطیل هستیم.</p>
        <div class="days" style="margin-bottom:1.25rem"></div>
        <div class="slots"></div>
        <input type="hidden" id="sel-date" name="date"><input type="hidden" id="sel-time" name="time">

        <div class="divider"></div>
        <h3>۲. شیوه برگزاری جلسه</h3>
        <div class="field" data-required-group>
          <div class="choice-grid">
            <label class="choice"><input type="radio" name="type" value="call" checked><span class="box">{ICONS["phone"]}<b>تماس تلفنی</b><small>ساده و سریع</small></span></label>
            <label class="choice"><input type="radio" name="type" value="video"><span class="box">{ICONS["video"]}<b>تماس تصویری</b><small>Google Meet / اسکایپ</small></span></label>
            <label class="choice"><input type="radio" name="type" value="chat"><span class="box">{ICONS["chat"]}<b>چت واتساپ</b><small>تبادل نمونه و ویس</small></span></label>
          </div>
        </div>

        <div class="divider"></div>
        <h3>۳. مشخصات شما</h3>
        <div class="form-grid">
          <div class="field"><label for="cname">نام و نام خانوادگی <span class="req">*</span></label><input id="cname" name="name" required><div class="err">نام را وارد کنید</div></div>
          <div class="field"><label for="cphone">شماره موبایل <span class="req">*</span></label><input id="cphone" name="phone" type="tel" required placeholder="09xx xxx xxxx" style="direction:ltr;text-align:right"><div class="err">شماره موبایل معتبر وارد کنید</div></div>
          <div class="field full">
            <label for="ctopic">موضوع اصلی مشاوره <span class="req">*</span></label>
            <select id="ctopic" name="topic" required>
              <option value="">انتخاب کنید…</option>
              <option>می‌خواهم اولین کتابم را چاپ کنم و نیاز به راهنمایی دارم</option>
              <option>برآورد هزینه و زمان طراحی جلد و صفحه‌آرایی</option>
              <option>انتخاب قطع، کاغذ و سبک بصری کتاب</option>
              <option>همکاری دوره‌ای انتشارات</option>
              <option>بررسی مشکل فنی فایل فعلی</option>
              <option>سایر موارد</option>
            </select><div class="err">موضوع مشاوره را انتخاب کنید</div>
          </div>
          <div class="field full"><label for="cnote">توضیح کوتاه <span class="opt">(اختیاری)</span></label><textarea id="cnote" name="note" style="min-height:100px" placeholder="هر نکته‌ای که کمک می‌کند جلسه برای‌تان پربارتر باشد…"></textarea></div>
        </div>
        <div style="margin-top:1.5rem"><button type="submit" class="btn btn-primary btn-lg btn-block">تأیید و ثبت نوبت مشاوره</button></div>
      </form>
    </div>

    <div id="consult-success" class="form-card success hidden">
      <div class="ok">{ICONS["check"]}</div>
      <h2>نوبت مشاوره‌ی شما ثبت شد ✅</h2>
      <p>زمان هماهنگ‌شده:</p>
      <div class="code" data-when>—</div>
      <p class="muted">پیامک یادآوری یک ساعت پیش از شروع جلسه برای‌تان ارسال خواهد شد.</p>
      <div style="display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap;margin-top:1.5rem">
        <a href="portfolio.html" class="btn btn-outline">مشاهده نمونه‌کارها</a>
        <a href="index.html" class="btn btn-primary">بازگشت به خانه</a>
      </div>
    </div>

    <aside class="sticky">
      <div class="side-card" style="display:flex;gap:1rem;align-items:center">
        <img src="assets/afra-hosseinzadeh.png" alt="افرا حسین‌زاده" width="614" height="820" style="width:68px;height:68px;border-radius:18px;object-fit:contain;background:var(--c-teal-light);flex-shrink:0">
        <div><b>افرا حسین‌زاده</b><p style="margin:0;font-size:.84rem">مدیر هنری، طراح جلد و صفحه‌آرا — ۱۰+ سال تجربه</p></div>
      </div>
      <div class="side-card">
        <h3>سرفصل‌های جلسه مشاوره</h3>
        <ul class="check-list">
          <li>{ICONS["check"]}<span>آشنایی با کتاب و هدف شما از انتشار</span></li>
          <li>{ICONS["check"]}<span>پیشنهاد قطع، کاغذ و نوع صحافی بهینه</span></li>
          <li>{ICONS["check"]}<span>برآورد شفاف هزینه و زمان‌بندی</span></li>
          <li>{ICONS["check"]}<span>راهنمای دریافت شابک، فیپا و مجوز</span></li>
        </ul>
      </div>
      <div class="side-card">
        <h3>تماس فوری</h3>
        <a href="tel:+989120000000" class="btn btn-outline btn-block" style="margin-bottom:.6rem">{ICONS["phone"]} <span dir="ltr">0912 000 0000</span></a>
        <a href="https://wa.me/989120000000" target="_blank" rel="noopener" class="btn btn-block" style="background:#25d366;color:#fff">{ICONS["wa"]} پیام در واتساپ</a>
      </div>
    </aside>
  </div>
</section>
"""
        + footer()
    )


# ======================================================
#  درباره افرا حسین‌زاده
# ======================================================
def about():
    return (
        head("درباره افرا حسین‌زاده", "بیوگرافی حرفه‌ای، مسیر کاری و تیم افرا حسین‌زاده؛ بیش از ده سال تجربه تخصصی در طراحی جلد و صفحه‌آرایی کتاب و مجله")
        + header()
        + page_hero("درباره من", "درباره‌ی افرا حسین‌زاده", "بیش از یک دهه همنشینی با کلمات، فونت‌های فارسی و بوی کاغذ چاپخانه.")
        + f"""
<section class="section--tight">
  <div class="container about-grid">
    <div class="about-img reveal">
      <img src="assets/afra-hosseinzadeh.png" width="614" height="820" alt="افرا حسین‌زاده">
      <div class="exp-badge"><b>۱۰+</b><small>سال تجربه</small></div>
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">داستان مسیر حرفه‌ای من</span>
      <h2>سلام، من افرا حسین‌زاده هستم</h2>
      <p>بیش از ده سال است که به صورت متمرکز در حوزه‌ی طراحی جلد و صفحه‌آرایی کتاب و نشریات فعالیت می‌کنم. در این سال‌ها افتخار همکاری با بیش از ۴۰ ناشر معتبر و صدها مؤلف و مترجم دغدغه‌مند را داشته‌ام و بیش از ۴۵۰ عنوان کتاب با طراحی و صفحه‌آرایی من راهی کتاب‌فروشی‌ها شده است.</p>
      <p>نگاه من به طراحی کتاب، نگاهی معمارانه است: جلد باید هویت اثر را در یک نگاه روایت کند و صفحه‌آرایی داخلی باید چنان روان و بی‌تکلف باشد که خواننده ساعت‌ها بدون خستگی چشم در متن غرق شود. با گسترش استودیو افرا گرافیک، این امکان فراهم شده تا نویسندگان مستقل نیز دقیقاً از همان استانداردهای حرفه‌ای نشر بهره‌مند شوند.</p>
      <div class="mini-stats">
        <div><b>+۴۵۰</b><span>کتاب صفحه‌آرایی‌شده</span></div>
        <div><b>+۳۲۰</b><span>جلد طراحی‌شده</span></div>
        <div><b>+۴۰</b><span>ناشر همکار</span></div>
        <div><b>۹۸٪</b><span>رضایت مشتریان</span></div>
      </div>
      <div class="tools" style="margin-top:2rem"><span>Adobe InDesign</span><span>Photoshop</span><span>Illustrator</span><span>Affinity Publisher</span><span>Figma</span><span>Procreate</span></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="sec-head center"><span class="eyebrow">اصول حرفه‌ای من</span><h2>چرا ناشران و مؤلفان همکاری با ما را ادامه می‌دهند؟</h2></div>
    <div class="grid-3">
      <div class="card reveal"><span class="ic" style="display:inline-grid;place-items:center;width:52px;height:52px;border-radius:14px;background:var(--c-teal-light);color:var(--c-teal);margin-bottom:1rem">{ICONS["shield"]}</span><h3>وسواس در تایپوگرافی فارسی</h3><p>رعایت دقیق نیم‌فاصله‌ها، جلوگیری از خطوط یتیم و بیوه، تراز خطوط کرسی و انتخاب فونت متناسب با ژانر اثر.</p></div>
      <div class="card reveal" data-delay="1"><span class="ic" style="display:inline-grid;place-items:center;width:52px;height:52px;border-radius:14px;background:var(--c-terra-light);color:var(--c-terra);margin-bottom:1rem">{ICONS["clock"]}</span><h3>تعهد کامل به تقویم نشر</h3><p>نمایشگاه کتاب و نوبت چاپخانه منتظر نمی‌مانند؛ بیش از ۹۵٪ پروژه‌ها زودتر از موعد مقرر تحویل شده‌اند.</p></div>
      <div class="card reveal" data-delay="2"><span class="ic" style="display:inline-grid;place-items:center;width:52px;height:52px;border-radius:14px;background:var(--c-gold-light);color:var(--c-gold);margin-bottom:1rem">{ICONS["chat"]}</span><h3>ارتباط مستقیم و شفاف</h3><p>از لحظه بریف تا تحویل فایل لیتوگرافی، ارتباط شفاف و گام‌به‌گام بدون هیچ هزینه‌ی پنهانی برقرار است.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container two-col" style="grid-template-columns:1fr 1fr">
    <div>
      <span class="eyebrow">مسیر رشد</span>
      <h2>از اولین کتاب تا شکل‌گیری استودیو</h2>
      <ul class="timeline" style="margin-top:1.5rem">
        <li><small>۱۳۹۲</small><b>آغاز مسیر حرفه‌ای</b><p>صفحه‌آرایی اولین مجموعه داستانی برای یک ناشر ادبی در تهران.</p></li>
        <li><small>۱۳۹۵</small><b>ورود به نشر حرفه‌ای و دانشگاهی</b><p>آغاز همکاری مستمر در طراحی یونیفرم و جلد برای انتشارات معتبر.</p></li>
        <li><small>۱۳۹۹</small><b>تکمیل حلقه تخصصی تیم</b><p>همراه شدن تصویرگر تخصصی کودک و ویراستار فنی با مجموعه.</p></li>
        <li><small>۱۴۰۲</small><b>پلتفرم آنلاین افرا گرافیک</b><p>ارائه خدمات مستقیم و آنلاین به نویسندگان مستقل در ایران و خارج از کشور.</p></li>
        <li><small>امروز</small><b>عبور از مرز ۴۵۰ عنوان کتاب</b><p>و همچنان شوق ورق زدن هر کتاب تازه از چاپ درآمده.</p></li>
      </ul>
    </div>
    <div>
      <span class="eyebrow">همکاران من</span>
      <h2>تیم همراه در استودیو افرا</h2>
      <div style="display:grid;gap:1rem;margin-top:1.5rem">
        <div class="card" style="display:flex;gap:1rem;align-items:center;padding:1.2rem"><img src="assets/afra-hosseinzadeh.png" alt="افرا حسین‌زاده" width="614" height="820" style="width:56px;height:56px;border-radius:16px;object-fit:contain;background:var(--c-teal-light);flex-shrink:0"><div><b>افرا حسین‌زاده</b><p style="margin:0;font-size:.88rem">بنیان‌گذار، مدیر هنری، طراح جلد و صفحه‌آرا</p></div></div>
        <div class="card" style="display:flex;gap:1rem;align-items:center;padding:1.2rem"><span class="av" style="width:56px;height:56px;border-radius:16px;background:var(--c-terra);color:#fff;display:grid;place-items:center;font-weight:900;font-size:1.3rem;flex-shrink:0">ن</span><div><b>نگار امینی</b><p style="margin:0;font-size:.88rem">تصویرگر کتاب کودک و طراح گرافیک</p></div></div>
        <div class="card" style="display:flex;gap:1rem;align-items:center;padding:1.2rem"><span class="av" style="width:56px;height:56px;border-radius:16px;background:var(--c-gold);color:#fff;display:grid;place-items:center;font-weight:900;font-size:1.3rem;flex-shrink:0">ر</span><div><b>رضا صادقی</b><p style="margin:0;font-size:.88rem">ویراستار فنی و نمونه‌خوان</p></div></div>
        <div class="card" style="display:flex;gap:1rem;align-items:center;padding:1.2rem"><span class="av" style="width:56px;height:56px;border-radius:16px;background:var(--c-ink-2);color:#fff;display:grid;place-items:center;font-weight:900;font-size:1.3rem;flex-shrink:0">م</span><div><b>مینا کاظمی</b><p style="margin:0;font-size:.88rem">هماهنگی پروژه و ارتباط با ناشران</p></div></div>
      </div>
    </div>
  </div>
</section>
{cta_block()}
"""
        + footer()
    )


# ======================================================
#  بلاگ
# ======================================================
def blog():
    return (
        head("مجله تخصصی", "مقالات و یادداشت‌های آموزشی افرا حسین‌زاده درباره طراحی جلد، صفحه‌آرایی، تایپوگرافی فارسی و راهنمای نشر کتاب")
        + header()
        + page_hero("مجله تخصصی", "مجله‌ی طراحی کتاب و نشر", "یادداشت‌ها و راهنماهای کاربردی درباره‌ی طراحی جلد، صفحه‌آرایی استاندارد و مسیر چاپ کتاب — به قلم افرا حسین‌زاده.")
        + f"""
<section class="section--tight">
  <div class="container">
    <div class="filters">{blog_filter_btns()}</div>
    <div class="blog-grid">{blog_cards()}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="cta reveal" style="text-align:right;display:grid;grid-template-columns:1.2fr 1fr;gap:2rem;align-items:center">
      <div><h2 style="font-size:1.7rem">خبرنامه‌ی ماهانه‌ی افرا حسین‌زاده</h2><p style="margin:0">هر ماه یک یادداشت تخصصی تایپوگرافی و بررسی کالبدشکافانه‌ی یک جلد کتاب. بدون هرزنامه.</p></div>
      <form data-simple="عضویت شما در خبرنامه ثبت شد ✅" style="display:flex;gap:.6rem;position:relative;flex-wrap:wrap" novalidate>
        <div class="field" style="flex:1;min-width:200px"><input type="email" required placeholder="ایمیل شما" style="direction:ltr;text-align:right;background:#fff;border-color:transparent;color:#141c1a"><div class="err" style="color:#ffd2cc">ایمیل معتبر وارد کنید</div></div>
        <button type="submit" class="btn btn-primary">عضویت</button>
      </form>
    </div>
  </div>
</section>
"""
        + footer()
    )


# ======================================================
#  تماس
# ======================================================
def contact():
    return (
        head("تماس با من", "راه‌های ارتباط مستقیم با افرا حسین‌زاده؛ تلفن، واتساپ، ایمیل و فرم تماس")
        + header()
        + page_hero("تماس", "ارتباط با افرا حسین‌زاده", "خوشحال می‌شوم درباره‌ی کتاب یا نشریه‌ی شما بشنوم. از هر طریقی که راحت‌تر هستید پیام بگذارید.")
        + f"""
<section class="section--tight">
  <div class="container">
    <div class="contact-cards">
      <a href="tel:+989120000000" class="ccard reveal"><span class="ic">{ICONS["phone"]}</span><b>تلفن و واتساپ</b><span>0912 000 0000</span></a>
      <a href="mailto:info@afradesigner.ir" class="ccard reveal" data-delay="1"><span class="ic" style="background:var(--c-terra-light);color:var(--c-terra)">{ICONS["mail"]}</span><b>ایمیل رسمی</b><span>info@afradesigner.ir</span></a>
      <div class="ccard reveal" data-delay="2"><span class="ic" style="background:var(--c-gold-light);color:var(--c-gold)">{ICONS["clock"]}</span><b>ساعات پاسخ‌گویی</b><span style="direction:rtl">شنبه تا پنج‌شنبه، ۱۰ تا ۱۸</span></div>
    </div>
    <div class="two-col" style="grid-template-columns:1.2fr 1fr">
      <form class="form-card" data-simple="پیام شما ارسال شد؛ به‌زودی پاسخ می‌دهیم ✅" novalidate>
        <h3>فرم ارسال پیام</h3>
        <p class="muted" style="font-size:.92rem">معمولاً ظرف چند ساعت کاری پاسخ می‌دهم.</p>
        <div class="form-grid">
          <div class="field"><label>نام و نام خانوادگی <span class="req">*</span></label><input name="name" required><div class="err">نام را وارد کنید</div></div>
          <div class="field"><label>موبایل یا ایمیل <span class="req">*</span></label><input name="contact" required style="direction:ltr;text-align:right"><div class="err">راه ارتباطی را وارد کنید</div></div>
          <div class="field full"><label>موضوع</label><select name="subject"><option>مشاوره و استعلام پروژه جدید</option><option>پیگیری سفارش ثبت‌شده</option><option>همکاری دوره‌ای انتشارات</option><option>پیشنهاد همکاری تخصصی</option><option>سایر</option></select></div>
          <div class="field full"><label>پیام شما <span class="req">*</span></label><textarea name="message" required></textarea><div class="err">متن پیام را وارد کنید</div></div>
        </div>
        <div style="margin-top:1.25rem"><button type="submit" class="btn btn-primary btn-lg">ارسال پیام</button></div>
      </form>
      <div>
        <div class="side-card">
          <h3>شبکه‌های اجتماعی افرا</h3>
          <p style="font-size:.92rem">پشت‌صحنه‌ی طراحی جلدها، اتودهای اولیه و نکات صفحه‌آرایی را در شبکه‌های اجتماعی دنبال کنید.</p>
          <div class="socials" style="margin-top:.5rem">
            <a href="https://instagram.com" target="_blank" rel="noopener" aria-label="اینستاگرام" style="background:var(--c-surface-2);color:var(--c-ink)">{ICONS["ig"]}</a>
            <a href="https://t.me" target="_blank" rel="noopener" aria-label="تلگرام" style="background:var(--c-surface-2);color:var(--c-ink)">{ICONS["tg"]}</a>
            <a href="https://wa.me/989120000000" target="_blank" rel="noopener" aria-label="واتساپ" style="background:var(--c-surface-2);color:var(--c-ink)">{ICONS["wa"]}</a>
            <a href="https://linkedin.com" target="_blank" rel="noopener" aria-label="لینکدین" style="background:var(--c-surface-2);color:var(--c-ink)">{ICONS["linkedin"]}</a>
          </div>
        </div>
        <div class="side-card">
          <h3>همکاری آنلاین با سراسر ایران و جهان</h3>
          <p style="font-size:.92rem;margin:0">تمامی مراحل از جلسه بریف تا تحویل فایل چاپی به صورت آنلاین و منظم انجام می‌شود. برای ناشران محترم در تهران امکان برگزاری جلسه حضوری با هماهنگی قبلی فراهم است.</p>
        </div>
        <div class="map-box" style="margin-top:1.25rem">
          <div class="text-center" style="padding:1rem">{ICONS["pin"].replace('viewBox', 'width="40" height="40" viewBox')}<p style="margin:.5rem 0 0">تهران — جلسه‌ی حضوری با هماهنگی قبلی</p></div>
        </div>
      </div>
    </div>
  </div>
</section>
{cta_block()}
"""
        + footer()
    )


PAGES = {
    "index.html": index,
    "services.html": services,
    "portfolio.html": portfolio,
    "order.html": order,
    "consult.html": consult,
    "about.html": about,
    "blog.html": blog,
    "contact.html": contact,
}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in PAGES.items():
        with open(os.path.join(here, name), "w", encoding="utf-8") as f:
            f.write(fn())
        print("✓", name)
