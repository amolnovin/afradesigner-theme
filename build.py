# -*- coding: utf-8 -*-
"""
اسکریپت ساخت صفحات استاتیک افرا گرافیک
اجرا:  python3 build.py
هدر و فوتر مشترک را در همه صفحات تزریق می‌کند.
"""
import os

ICONS = {
    "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5"/><path d="m12 19-7-7 7-7"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg>',
    "layout": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18M9 21V9"/></svg>',
    "mag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 6h4M2 10h4M2 14h4M2 18h4"/><rect width="16" height="20" x="4" y="2" rx="2"/><path d="M15 2v20M9 7h3M9 11h3"/></svg>',
    "tablet": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="16" height="20" x="4" y="2" rx="2"/><path d="M12 18h.01"/></svg>',
    "edit": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>',
    "print": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect width="12" height="8" x="6" y="14"/></svg>',
    "upload": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m17 8-5-5-5 5M12 3v12"/></svg>',
    "sun": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>',
    "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4M12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 0 1 2.2 12C2.2 6.6 6.6 2.2 12 2.2S21.8 6.6 21.8 12 17.4 21.8 12 21.8M12 0C5.4 0 0 5.4 0 12c0 2.1.6 4.2 1.6 6L0 24l6.2-1.6c1.8 1 3.8 1.5 5.8 1.5 6.6 0 12-5.4 12-12S18.6 0 12 0"/></svg>',
    "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="20" x="2" y="2" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/></svg>',
    "tg": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.4 18.7 19.6c-.2 1-.9 1.3-1.8.8l-5-3.7-2.4 2.3c-.3.3-.5.5-1 .5l.4-5.1L18 6.1c.4-.4-.1-.6-.6-.2L5.9 13.1 1 11.6c-1.1-.3-1.1-1.1.2-1.6L20.5 2.6c.9-.3 1.7.2 1.4 1.8"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9v5.7H9.3V9h3.4v1.6c.5-.9 1.6-1.8 3.4-1.8 3.6 0 4.3 2.4 4.3 5.5v6.2ZM5.3 7.4a2.1 2.1 0 1 1 0-4.1 2.1 2.1 0 0 1 0 4.1M7.1 20.5H3.5V9h3.6ZM22.2 0H1.8C.8 0 0 .8 0 1.7v20.5c0 1 .8 1.8 1.8 1.8h20.4c1 0 1.8-.8 1.8-1.8V1.7C24 .8 23.2 0 22.2 0"/></svg>',
    "up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m18 15-6-6-6 6"/></svg>',
    "star": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    "video": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m22 8-6 4 6 4V8Z"/><rect width="14" height="12" x="2" y="6" rx="2"/></svg>',
    "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
}

NAV = [
    ("index.html", "خانه"),
    ("services.html", "خدمات و تعرفه"),
    ("portfolio.html", "نمونه‌کارها"),
    ("consult.html", "مشاوره رایگان"),
    ("about.html", "درباره افرا"),
    ("blog.html", "مجله"),
    ("contact.html", "تماس"),
]

def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl" data-theme="auto">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | افرا گرافیک — طراحی جلد و صفحه‌آرایی کتاب</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1f5f63">
<meta property="og:title" content="{title} | افرا گرافیک">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%231f5f63'/%3E%3Cpath d='M32 50A18 18 0 0 1 29 14c14-3 18-4 23-10 2 5 5 10 5 20 0 14-12 26-25 26Z' fill='%23fff'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
"""

def header():
    links = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    mlinks = "".join(f'<a href="{h}">{t}<span>{ICONS["arrow"]}</span></a>'.replace('<span><svg', '<span style="width:18px;display:inline-block"><svg') for h, t in NAV)
    return f"""
<header class="header">
  <div class="container nav">
    <a href="index.html" class="logo" aria-label="افرا گرافیک">
      <span class="logo-mark">{ICONS["leaf"]}</span>
      <span>افرا گرافیک<small>طراحی جلد و صفحه‌آرایی</small></span>
    </a>
    <nav class="nav-links" aria-label="منوی اصلی">{links}</nav>
    <div class="nav-actions">
      <button class="icon-btn" data-theme-toggle aria-label="تغییر تم">{ICONS["sun"]}</button>
      <a href="order.html" class="btn btn-primary nav-cta">ثبت سفارش</a>
      <button class="icon-btn burger" data-menu-open aria-label="باز کردن منو">{ICONS["menu"]}</button>
    </div>
  </div>
</header>
<div class="mobile-menu" aria-hidden="true">
  <div class="top">
    <a href="index.html" class="logo"><span class="logo-mark">{ICONS["leaf"]}</span><span>افرا گرافیک</span></a>
    <button class="icon-btn" data-menu-close aria-label="بستن">{ICONS["x"]}</button>
  </div>
  <nav>{mlinks}</nav>
  <div class="bottom">
    <a href="order.html" class="btn btn-primary btn-lg">ثبت سفارش</a>
    <a href="consult.html" class="btn btn-outline">رزرو مشاوره رایگان</a>
  </div>
</div>
<main>
"""

def footer():
    return f"""
</main>
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a href="index.html" class="logo"><span class="logo-mark">{ICONS["leaf"]}</span><span>افرا گرافیک<small>طراحی جلد و صفحه‌آرایی</small></span></a>
        <p style="margin-top:1rem">بیش از ده سال تجربه در طراحی جلد و صفحه‌آرایی کتاب و مجله برای ناشران و نویسندگان مستقل. کتاب شما را همان‌طور که شایسته‌اش است، آماده چاپ می‌کنیم.</p>
        <div class="socials">
          <a href="#" aria-label="اینستاگرام">{ICONS["ig"]}</a>
          <a href="#" aria-label="تلگرام">{ICONS["tg"]}</a>
          <a href="#" aria-label="واتساپ">{ICONS["wa"]}</a>
          <a href="#" aria-label="لینکدین">{ICONS["linkedin"]}</a>
        </div>
      </div>
      <div>
        <h4>دسترسی سریع</h4>
        <ul>
          <li><a href="services.html">خدمات و تعرفه</a></li>
          <li><a href="portfolio.html">نمونه‌کارها</a></li>
          <li><a href="order.html">ثبت سفارش</a></li>
          <li><a href="consult.html">مشاوره رایگان</a></li>
          <li><a href="about.html">درباره افرا</a></li>
          <li><a href="blog.html">مجله</a></li>
        </ul>
      </div>
      <div>
        <h4>خدمات</h4>
        <ul>
          <li><a href="services.html#cover">طراحی جلد کتاب</a></li>
          <li><a href="services.html#layout">صفحه‌آرایی کتاب</a></li>
          <li><a href="services.html#magazine">صفحه‌آرایی مجله</a></li>
          <li><a href="services.html#ebook">کتاب الکترونیک</a></li>
          <li><a href="services.html#print">آماده‌سازی چاپ</a></li>
        </ul>
      </div>
      <div>
        <h4>ارتباط با ما</h4>
        <ul class="contact-list">
          <li>{ICONS["phone"]}<span dir="ltr">0912 000 0000</span></li>
          <li>{ICONS["mail"]}<span>info@afradesigner.ir</span></li>
          <li>{ICONS["clock"]}<span>شنبه تا پنج‌شنبه — ۱۰ تا ۱۸</span></li>
          <li>{ICONS["pin"]}<span>تهران — همکاری آنلاین با سراسر ایران</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year></span> افرا گرافیک — تمامی حقوق محفوظ است.</span>
      <span>afradesigner.ir</span>
    </div>
  </div>
</footer>
<a href="https://wa.me/989120000000" class="fab-wa" target="_blank" rel="noopener" aria-label="گفتگو در واتساپ">{ICONS["wa"]}</a>
<button class="to-top" aria-label="بازگشت به بالا">{ICONS["up"]}</button>
<div class="toast" role="status"></div>
<script src="js/main.js"></script>
</body>
</html>
"""

def page_hero(crumb, title, lead):
    return f"""
<section class="page-hero text-center">
  <div class="container">
    <nav class="breadcrumb"><a href="index.html">خانه</a><span>/</span><span>{crumb}</span></nav>
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
      <h2>آماده‌اید کتاب‌تان را حرفه‌ای ببینید؟</h2>
      <p>در کمتر از ۵ دقیقه سفارش‌تان را ثبت کنید یا یک جلسه مشاوره رایگان ۲۰ دقیقه‌ای رزرو کنید تا با هم بهترین مسیر را پیدا کنیم.</p>
      <div class="actions">
        <a href="order.html" class="btn btn-primary btn-lg">ثبت سفارش</a>
        <a href="consult.html" class="btn btn-outline btn-lg">مشاوره رایگان</a>
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

def work_cards(limit=None, cls=""):
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
    return "".join(f'<button class="filter-btn{" active" if k=="all" else ""}" data-filter="{k}">{v}</button>' for k, v in FILTERS)

# ======================================================
#  صفحه اصلی
# ======================================================
def index():
    return head("خانه", "طراحی جلد و صفحه‌آرایی حرفه‌ای کتاب و مجله با بیش از ۱۰ سال تجربه — افرا حسین‌زاده") + header() + f"""
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">استودیو طراحی جلد و صفحه‌آرایی</span>
      <h1>کتاب شما شایسته‌ی <span class="hl">یک جلد ماندگار</span> و صفحاتی خوش‌خوان است</h1>
      <p class="lead">سلام، من <strong>افرا حسین‌زاده</strong> هستم. بیش از ده سال است که با ناشران و نویسندگان مستقل همکاری می‌کنم تا کتاب‌ها و مجله‌ها دقیق، زیبا و آماده‌ی چاپ شوند — در کمترین زمان و با خیال راحت.</p>
      <div class="hero-actions">
        <a href="order.html" class="btn btn-primary btn-lg">ثبت سفارش آنلاین</a>
        <a href="portfolio.html" class="btn btn-outline btn-lg">مشاهده نمونه‌کارها</a>
      </div>
      <div class="hero-trust">
        <div class="avatars"><span>ن</span><span>م</span><span>س</span><span>+</span></div>
        <div><span class="stars">★★★★★</span> رضایت بیش از <b>۲۰۰</b> ناشر و نویسنده</div>
      </div>
    </div>
    <div class="hero-visual">
      <img class="main-img" src="assets/hero.jpg" alt="نمونه کتاب‌های طراحی‌شده توسط افرا گرافیک">
      <div class="float-card one">
        <span class="ic" style="background:var(--c-teal-light);color:var(--c-teal)">{ICONS["book"]}</span>
        <div><b>+۴۵۰</b><small>کتاب آماده‌ی چاپ</small></div>
      </div>
      <div class="float-card two">
        <span class="ic" style="background:var(--c-terra-light);color:var(--c-terra)">{ICONS["clock"]}</span>
        <div><b>۴۸ ساعت</b><small>تحویل اولین طرح جلد</small></div>
      </div>
    </div>
  </div>
</section>

<section class="trusted">
  <div class="container">
    <div class="lbl">افتخار همکاری با انتشارات و مجموعه‌های معتبر</div>
    <div class="marquee"><div class="marquee-track">
      <span>نشر چشمه</span><span>نشر نگاه</span><span>انتشارات سمت</span><span>نشر مروارید</span><span>کانون پرورش فکری</span><span>نشر ققنوس</span><span>نشر ثالث</span><span>نشر افق</span>
      <span>نشر چشمه</span><span>نشر نگاه</span><span>انتشارات سمت</span><span>نشر مروارید</span><span>کانون پرورش فکری</span><span>نشر ققنوس</span><span>نشر ثالث</span><span>نشر افق</span>
    </div></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="stats">
      <div class="stat reveal"><b data-count="10" data-suffix="+">۰</b><span>سال تجربه</span></div>
      <div class="stat reveal" data-delay="1"><b data-count="450" data-suffix="+">۰</b><span>کتاب صفحه‌آرایی‌شده</span></div>
      <div class="stat reveal" data-delay="2"><b data-count="320" data-suffix="+">۰</b><span>جلد طراحی‌شده</span></div>
      <div class="stat reveal" data-delay="3"><b data-count="98" data-suffix="٪">۰</b><span>رضایت مشتریان</span></div>
    </div>
  </div>
</section>

<section class="section section--alt" id="services">
  <div class="container">
    <div class="sec-head center">
      <span class="eyebrow">خدمات ما</span>
      <h2>هر آن‌چه کتاب‌تان برای رسیدن به قفسه نیاز دارد</h2>
      <p>از ایده‌ی اولیه‌ی جلد تا فایل نهایی آماده‌ی چاپخانه — همه‌چیز در یک جا، با یک تیم.</p>
    </div>
    <div class="services-grid">
      <article class="service-card reveal">
        <span class="ic">{ICONS["book"]}</span>
        <h3>طراحی جلد کتاب</h3>
        <p>جلدی که در قفسه دیده شود و در دست، حس اعتماد بدهد؛ متناسب با ژانر و مخاطب کتاب.</p>
        <ul><li>۳ اتود اولیه + ویرایش نامحدود</li><li>طراحی پشت جلد و عطف</li><li>فایل آماده‌ی چاپ با خط برش</li></ul>
        <div class="price">از ۳٫۵ میلیون تومان <small>/ پروژه</small></div>
      </article>
      <article class="service-card terra reveal" data-delay="1">
        <span class="ic">{ICONS["layout"]}</span>
        <h3>صفحه‌آرایی کتاب</h3>
        <p>چیدمان حرفه‌ای متن در ایندیزاین با رعایت اصول تایپوگرافی فارسی و استانداردهای چاپ.</p>
        <ul><li>انتخاب فونت و گرید اختصاصی</li><li>فهرست، پانویس و نمایه</li><li>خروجی PDF چاپ + ای‌بوک</li></ul>
        <div class="price">از ۱۸ هزار تومان <small>/ صفحه</small></div>
      </article>
      <article class="service-card gold reveal" data-delay="2">
        <span class="ic">{ICONS["mag"]}</span>
        <h3>صفحه‌آرایی مجله و نشریه</h3>
        <p>طراحی ادیتوریال پویا برای مجلات، کاتالوگ و گزارش‌های سالانه با هویت بصری یک‌پارچه.</p>
        <ul><li>طراحی تمپلیت و مستر‌پیج</li><li>اینفوگرافیک و جداول</li><li>هماهنگی با چاپخانه</li></ul>
        <div class="price">از ۴۵ هزار تومان <small>/ صفحه</small></div>
      </article>
    </div>
    <div class="text-center" style="margin-top:2.5rem"><a href="services.html" class="btn btn-ghost">مشاهده همه خدمات و تعرفه‌ها {ICONS["arrow"]}</a></div>
  </div>
</section>

<section class="section" id="portfolio">
  <div class="container">
    <div class="sec-head center">
      <span class="eyebrow">نمونه‌کارها</span>
      <h2>پیش از تصمیم، کارهای ما را ببینید</h2>
      <p>گزیده‌ای از پروژه‌های اخیر؛ روی هر نمونه کلیک کنید تا جزئیات را ببینید.</p>
    </div>
    <div class="filters">{filters()}</div>
    <div class="work-grid">{work_cards()}</div>
    <div class="work-more"><a href="portfolio.html" class="btn btn-outline btn-lg">مشاهده همه نمونه‌کارها</a></div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="sec-head center">
      <span class="eyebrow">فرآیند کار</span>
      <h2>در چهار قدم ساده، کتاب‌تان آماده‌ی چاپ می‌شود</h2>
    </div>
    <div class="steps">
      <div class="step reveal"><h3>ثبت سفارش و بریف</h3><p>فرم سفارش را پر می‌کنید یا در جلسه‌ی مشاوره درباره‌ی کتاب، مخاطب و سلیقه‌تان صحبت می‌کنیم.</p></div>
      <div class="step reveal" data-delay="1"><h3>اتود و پیش‌نمایش</h3><p>ظرف ۴۸ ساعت اتودهای اولیه‌ی جلد یا نمونه‌ی چند صفحه از صفحه‌آرایی را دریافت می‌کنید.</p></div>
      <div class="step reveal" data-delay="2"><h3>بازخورد و اصلاح</h3><p>نظرات‌تان را اعمال می‌کنیم؛ تا زمانی که کاملاً راضی باشید، اصلاحات ادامه دارد.</p></div>
      <div class="step reveal" data-delay="3"><h3>تحویل فایل نهایی</h3><p>فایل‌های آماده‌ی چاپ (PDF/X)، فایل باز و نسخه‌ی دیجیتال را تحویل می‌گیرید.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container about-grid">
    <div class="about-img reveal">
      <img src="assets/designer.jpg" alt="افرا حسین‌زاده — طراح جلد و صفحه‌آرا">
      <div class="exp-badge"><b>۱۰+</b><small>سال تجربه</small></div>
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">درباره افرا</span>
      <h2>عاشق صفحه‌آرایی‌ام و عاشق کتاب خواندن</h2>
      <p>به نظرم لذت‌بخش‌ترین کار دنیا، کار کردن با کلمات است. بیش از ده سال است که در حوزه‌ی طراحی جلد و صفحه‌آرایی کتاب و مجله فعالیت می‌کنم و با ناشران زیادی همکاری داشته‌ام. حالا با تیم طراحی‌ام تصمیم گرفته‌ایم فعالیت‌مان را گسترده‌تر کنیم تا نویسندگان مستقل هم به کیفیتی حرفه‌ای دسترسی داشته باشند.</p>
      <div class="skills">
        <div class="skill" style="--w:98%"><div class="lbl"><span>صفحه‌آرایی (InDesign)</span><span>۹۸٪</span></div><div class="bar"><i></i></div></div>
        <div class="skill" style="--w:95%"><div class="lbl"><span>طراحی جلد</span><span>۹۵٪</span></div><div class="bar"><i></i></div></div>
        <div class="skill" style="--w:90%"><div class="lbl"><span>تایپوگرافی فارسی</span><span>۹۰٪</span></div><div class="bar"><i></i></div></div>
      </div>
      <div class="tools"><span>Adobe InDesign</span><span>Photoshop</span><span>Illustrator</span><span>Affinity</span><span>Figma</span></div>
      <div style="margin-top:2rem"><a href="about.html" class="btn btn-primary">بیشتر درباره ما</a></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="sec-head center">
      <span class="eyebrow">نظر مشتریان</span>
      <h2>ناشران و نویسندگان چه می‌گویند؟</h2>
    </div>
    <div class="testi-wrap">
      <div class="testi-track">
        <article class="testi"><span class="quote">“</span><p>صفحه‌آرایی کتاب ۴۰۰ صفحه‌ای ما در کمتر از دو هفته با کیفیتی عالی تحویل شد. دقت افرا در جزئیات تایپوگرافی فارسی واقعاً کم‌نظیر است.</p><div class="who"><span class="av">م</span><div><b>مریم رضایی</b><small>مدیر تولید نشر نگاه</small></div></div></article>
        <article class="testi"><span class="quote">“</span><p>اولین کتابم بود و هیچ تجربه‌ای نداشتم. جلسه‌ی مشاوره‌ی رایگان همه‌چیز را روشن کرد و جلد نهایی دقیقاً همان چیزی شد که در ذهنم بود.</p><div class="who"><span class="av" style="background:var(--c-terra)">ع</span><div><b>علی محمدی</b><small>نویسنده‌ی مستقل</small></div></div></article>
        <article class="testi"><span class="quote">“</span><p>برای ماهنامه‌مان تمپلیت جدیدی طراحی شد که هم زیباست و هم کار تیم را برای شماره‌های بعدی خیلی سریع کرده.</p><div class="who"><span class="av" style="background:var(--c-gold)">س</span><div><b>سارا کریمی</b><small>سردبیر ماهنامه هنر و اندیشه</small></div></div></article>
        <article class="testi"><span class="quote">“</span><p>سه چاپ از کتاب درسی ما با همین صفحه‌آرایی منتشر شده و همیشه بازخورد دانشجوها درباره‌ی خوانایی متن مثبت بوده.</p><div class="who"><span class="av" style="background:var(--c-ink-2)">د</span><div><b>دکتر حمید احمدی</b><small>عضو هیئت علمی</small></div></div></article>
      </div>
      <div class="testi-ctrl">
        <button class="icon-btn" data-testi="prev" aria-label="قبلی">{ICONS["arrow"].replace('<path d="M19 12H5"/><path d="m12 19-7-7 7-7"/>', '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>')}</button>
        <button class="icon-btn" data-testi="next" aria-label="بعدی">{ICONS["arrow"]}</button>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head center"><span class="eyebrow">سؤالات متداول</span><h2>پاسخ سؤال‌های رایج شما</h2></div>
    <div class="faq">
      <details><summary>هزینه‌ی طراحی جلد و صفحه‌آرایی چطور محاسبه می‌شود؟</summary><div class="ans">هزینه‌ی صفحه‌آرایی بر اساس تعداد صفحه، پیچیدگی متن (جدول، فرمول، تصویر) و زمان تحویل محاسبه می‌شود. طراحی جلد قیمت پایه‌ی ثابت دارد. در <a href="services.html" style="color:var(--c-teal)">صفحه‌ی تعرفه</a> ماشین‌حساب برآورد قیمت قرار داده‌ایم.</div></details>
      <details><summary>چقدر طول می‌کشد؟</summary><div class="ans">اتود اولیه‌ی جلد معمولاً ظرف ۴۸ ساعت آماده می‌شود. صفحه‌آرایی یک کتاب ۲۰۰ صفحه‌ای متنی حدود ۵ تا ۷ روز کاری زمان می‌برد. برای پروژه‌های فوری، گزینه‌ی تحویل سریع داریم.</div></details>
      <details><summary>چند بار می‌توانم درخواست اصلاح بدهم؟</summary><div class="ans">تا زمانی که از نتیجه راضی باشید. ما تا رسیدن به نتیجه‌ی مطلوب در چارچوب بریف اولیه، اصلاحات را بدون هزینه‌ی اضافه انجام می‌دهیم.</div></details>
      <details><summary>چه فایل‌هایی تحویل می‌گیرم؟</summary><div class="ans">PDF آماده‌ی چاپ با خط برش و رنگ CMYK، فایل باز ایندیزاین/فتوشاپ، نسخه‌ی RGB برای فضای دیجیتال و در صورت درخواست، فایل EPUB.</div></details>
      <details><summary>آیا برای گرفتن مجوز و شابک هم کمک می‌کنید؟</summary><div class="ans">بله؛ اگر نویسنده‌ی مستقل هستید، در جلسه‌ی مشاوره مسیر گرفتن شابک، فیپا و همکاری با ناشر یا چاپخانه را برای‌تان توضیح می‌دهیم.</div></details>
    </div>
  </div>
</section>
{cta_block()}
""" + footer()

# ======================================================
#  خدمات و تعرفه
# ======================================================
def services():
    def svc(id_, icon, cls, title, desc, items, price, img=None):
        return f"""
    <article class="service-card {cls} reveal" id="{id_}">
      <span class="ic">{ICONS[icon]}</span>
      <h3>{title}</h3>
      <p>{desc}</p>
      <ul>{"".join(f"<li>{i}</li>" for i in items)}</ul>
      <div class="price">{price}</div>
      <div style="margin-top:1.2rem"><a href="order.html" class="btn btn-sm btn-primary">سفارش این خدمت</a></div>
    </article>"""
    return head("خدمات و تعرفه", "لیست کامل خدمات طراحی جلد، صفحه‌آرایی کتاب و مجله، کتاب الکترونیک و آماده‌سازی چاپ به همراه تعرفه و ماشین‌حساب برآورد قیمت") + header() + page_hero("خدمات و تعرفه", "خدمات و تعرفه‌ها", "قیمت‌ها شفاف و بدون هزینه‌ی پنهان است. برآورد دقیق پس از بررسی فایل شما اعلام می‌شود.") + f"""
<section class="section--tight">
  <div class="container services-grid">
    {svc("cover", "book", "", "طراحی جلد کتاب", "طراحی اختصاصی جلد متناسب با ژانر، مخاطب و هویت ناشر؛ شامل روی جلد، پشت جلد و عطف.", ["۳ اتود اولیه با رویکردهای متفاوت", "ویرایش نامحدود تا رضایت کامل", "طراحی عطف با محاسبه‌ی دقیق ضخامت", "فایل چاپ CMYK با خط برش و لب‌برگرد", "نسخه‌ی موکاپ سه‌بعدی برای معرفی"], "از ۳٫۵ میلیون تومان <small>/ پروژه</small>")}
    {svc("layout", "layout", "terra", "صفحه‌آرایی کتاب", "چیدمان حرفه‌ای متن در Adobe InDesign با رعایت اصول تایپوگرافی فارسی و استانداردهای چاپ.", ["انتخاب فونت، اندازه و گرید اختصاصی", "طراحی صفحات آغازین، فهرست و شناسنامه", "پانویس، نمایه، جدول و تصویر", "نمونه‌خوانی چیدمان پیش از تحویل", "خروجی PDF چاپ + نسخه‌ی دیجیتال"], "از ۱۸ هزار تومان <small>/ صفحه</small>")}
    {svc("magazine", "mag", "gold", "صفحه‌آرایی مجله و کاتالوگ", "طراحی ادیتوریال پویا برای مجلات، کاتالوگ محصولات و گزارش‌های سالانه.", ["طراحی تمپلیت و مسترپیج قابل استفاده‌ی مجدد", "گرید چندستونه، نقل‌قول و اینفوگرافیک", "رتوش و آماده‌سازی تصاویر", "هماهنگی فنی با چاپخانه"], "از ۴۵ هزار تومان <small>/ صفحه</small>")}
    {svc("ebook", "tablet", "", "کتاب الکترونیک (EPUB / PDF)", "تبدیل کتاب به نسخه‌ی دیجیتال استاندارد برای طاقچه، فیدیبو و کیندل.", ["EPUB واکنش‌گرا با پشتیبانی فارسی", "PDF تعاملی با فهرست کلیک‌شونده", "بهینه‌سازی حجم تصاویر", "تست روی دستگاه‌های مختلف"], "از ۱۲ هزار تومان <small>/ صفحه</small>")}
    {svc("edit", "edit", "terra", "ویراستاری و نمونه‌خوانی", "ویرایش صوری و فنی متن پیش از صفحه‌آرایی برای متنی پاکیزه و یک‌دست.", ["اصلاح رسم‌الخط و نشانه‌گذاری", "یک‌دست‌سازی نیم‌فاصله و اعداد", "بررسی ارجاعات و پانویس‌ها"], "از ۶ هزار تومان <small>/ صفحه</small>")}
    {svc("print", "print", "gold", "آماده‌سازی و نظارت چاپ", "بررسی فنی فایل، پروف رنگی و همراهی تا خروج کتاب از چاپخانه.", ["Preflight فنی فایل نهایی", "مشاوره‌ی انتخاب کاغذ و جلد", "معرفی چاپخانه‌های همکار", "بررسی نمونه‌ی چاپی (پروف)"], "توافقی <small>/ بسته به تیراژ</small>")}
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head center"><span class="eyebrow">بسته‌های پیشنهادی</span><h2>بسته‌ای متناسب با کتاب‌تان انتخاب کنید</h2><p>برای کتاب‌های متنی تا ۲۰۰ صفحه. برای پروژه‌های بزرگ‌تر، قیمت اختصاصی اعلام می‌شود.</p></div>
    <div class="pricing">
      <div class="plan reveal">
        <h3>پایه</h3>
        <div class="p">۴٫۹ <small>میلیون تومان</small></div>
        <p class="desc">مناسب نویسندگان مستقل با بودجه‌ی محدود</p>
        <ul><li>صفحه‌آرایی تا ۲۰۰ صفحه‌ی متنی</li><li>طراحی جلد (۲ اتود)</li><li>۲ دور اصلاح</li><li>فایل چاپ PDF</li><li class="no">فایل باز ایندیزاین</li><li class="no">نسخه‌ی EPUB</li></ul>
        <a href="order.html" class="btn btn-outline btn-block">انتخاب بسته</a>
      </div>
      <div class="plan featured reveal" data-delay="1">
        <span class="badge">محبوب‌ترین</span>
        <h3>حرفه‌ای</h3>
        <div class="p">۷٫۹ <small>میلیون تومان</small></div>
        <p class="desc">انتخاب اکثر ناشران و نویسندگان</p>
        <ul><li>صفحه‌آرایی تا ۲۰۰ صفحه (با جدول و تصویر)</li><li>طراحی جلد (۳ اتود) + عطف و پشت جلد</li><li>اصلاح نامحدود</li><li>فایل چاپ + فایل باز</li><li>نسخه‌ی EPUB</li><li>موکاپ سه‌بعدی برای معرفی</li></ul>
        <a href="order.html" class="btn btn-primary btn-block">انتخاب بسته</a>
      </div>
      <div class="plan reveal" data-delay="2">
        <h3>ناشران</h3>
        <div class="p">توافقی</div>
        <p class="desc">قرارداد بلندمدت برای مجموعه‌ی عناوین</p>
        <ul><li>تخفیف پلکانی بر اساس تعداد عنوان</li><li>طراحی هویت بصری مجموعه</li><li>اولویت در زمان‌بندی</li><li>مدیر پروژه‌ی اختصاصی</li><li>نظارت چاپ</li><li>گزارش ماهانه</li></ul>
        <a href="consult.html" class="btn btn-outline btn-block">درخواست جلسه</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container two-col">
    <div>
      <span class="eyebrow">ماشین‌حساب</span>
      <h2>برآورد سریع هزینه</h2>
      <p>مشخصات کتاب‌تان را وارد کنید تا یک برآورد تقریبی ببینید. قیمت نهایی پس از بررسی فایل اعلام می‌شود.</p>
      <form id="calc" class="form-card" style="box-shadow:none">
        <div class="form-grid">
          <div class="field">
            <label>نوع اثر</label>
            <select name="type"><option value="book">کتاب متنی (رمان، داستان، شعر)</option><option value="academic">کتاب دانشگاهی / علمی</option><option value="kids">کتاب کودک (مصور)</option><option value="magazine">مجله / کاتالوگ</option><option value="ebook">فقط کتاب الکترونیک</option></select>
          </div>
          <div class="field">
            <label>تعداد صفحات</label>
            <input type="number" name="pages" min="1" value="200">
          </div>
          <div class="field full" style="display:flex;gap:1.5rem;flex-wrap:wrap">
            <label style="display:flex;align-items:center;gap:.5rem;font-weight:600"><input type="checkbox" name="cover" checked style="width:18px;height:18px;accent-color:var(--c-teal)"> طراحی جلد هم می‌خواهم</label>
            <label style="display:flex;align-items:center;gap:.5rem;font-weight:600"><input type="checkbox" name="edit" style="width:18px;height:18px;accent-color:var(--c-teal)"> نمونه‌خوانی و ویرایش صوری</label>
          </div>
        </div>
        <div class="estimate"><div><small>برآورد تقریبی</small><b id="calc-out">—</b></div><a href="order.html" class="btn btn-primary">ثبت سفارش با این مشخصات</a></div>
      </form>
    </div>
    <aside class="sticky">
      <div class="side-card">
        <h3>در همه‌ی خدمات شامل می‌شود</h3>
        <ul class="check-list">
          <li>{ICONS["check"]}جلسه‌ی مشاوره‌ی رایگان اولیه</li>
          <li>{ICONS["check"]}قرارداد رسمی و زمان‌بندی مشخص</li>
          <li>{ICONS["check"]}پیش‌نمایش پیش از پرداخت نهایی</li>
          <li>{ICONS["check"]}پشتیبانی ۳۰ روزه پس از تحویل</li>
          <li>{ICONS["check"]}محرمانگی کامل محتوای اثر</li>
        </ul>
      </div>
      <div class="side-card" style="background:var(--c-teal);color:#fff;border:0">
        <h3 style="color:#fff">مطمئن نیستید کدام را انتخاب کنید؟</h3>
        <p style="color:rgba(255,255,255,.8);font-size:.92rem">در یک تماس ۲۰ دقیقه‌ای رایگان درباره‌ی کتاب‌تان صحبت می‌کنیم.</p>
        <a href="consult.html" class="btn btn-block" style="background:#fff;color:var(--c-teal-dark)">رزرو مشاوره</a>
      </div>
    </aside>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="sec-head center"><span class="eyebrow">جزئیات</span><h2>جدول مقایسه‌ی تعرفه‌ی صفحه‌آرایی</h2></div>
    <div class="table-wrap">
      <table class="table">
        <thead><tr><th>نوع محتوا</th><th>قیمت هر صفحه</th><th>زمان تقریبی (۲۰۰ صفحه)</th><th>توضیح</th></tr></thead>
        <tbody>
          <tr><td>متن ساده (رمان، داستان)</td><td>۱۸٬۰۰۰ تومان</td><td>۵ روز کاری</td><td>بدون جدول و تصویر</td></tr>
          <tr><td>متن با پانویس و ارجاع</td><td>۲۲٬۰۰۰ تومان</td><td>۷ روز کاری</td><td>کتب دانشگاهی و پژوهشی</td></tr>
          <tr><td>متن با جدول، فرمول و نمودار</td><td>۲۸٬۰۰۰ تومان</td><td>۱۰ روز کاری</td><td>کتب فنی و مهندسی</td></tr>
          <tr><td>شعر (کلاسیک و نو)</td><td>۱۵٬۰۰۰ تومان</td><td>۴ روز کاری</td><td>چیدمان مصرع و بیت</td></tr>
          <tr><td>کتاب کودک مصور</td><td>۶۰٬۰۰۰ تومان</td><td>۱۰ روز کاری</td><td>ترکیب تصویر و لترینگ</td></tr>
          <tr><td>مجله / کاتالوگ</td><td>۴۵٬۰۰۰ تومان</td><td>۷ روز کاری</td><td>طراحی ادیتوریال</td></tr>
        </tbody>
      </table>
    </div>
    <p class="muted text-center" style="margin-top:1rem;font-size:.85rem">* تحویل فوری (نصف زمان) با ۳۰٪ افزایش قیمت و تحویل خیلی فوری با ۶۰٪ افزایش قیمت انجام می‌شود.</p>
  </div>
</section>
{cta_block()}
""" + footer()

# ======================================================
#  نمونه‌کارها
# ======================================================
def portfolio():
    extra = WORKS + [
        ("cover-2.jpg", "cover", "طراحی جلد", "مجموعه شعر «سایه‌ی سرو»", "بازطراحی جلد برای چاپ ششم با حفظ هویت نسخه‌ی اصلی", "نشر ثالث | شومیز | رقعی", False),
        ("layout-1.jpg", "academic", "دانشگاهی", "مبانی اقتصاد خرد", "صفحه‌آرایی ۵۲۰ صفحه با ۱۴۰ جدول و نمودار", "انتشارات سمت | وزیری | ۱۴۰۳", False),
        ("cover-1.jpg", "cover", "طراحی جلد", "رمان «باران در آبان»", "جلد مینیمال با بافت کاغذ و طلاکوب", "نشر افق | جلد سخت | رقعی", False),
    ]
    cards = ""
    for i, (img, cat, cat_label, title, desc, meta, wide) in enumerate(extra):
        cards += f"""
      <article class="work reveal{" wide" if wide else ""}" data-cat="{cat}" data-cat-label="{cat_label}" data-title="{title}" data-desc="{desc}" data-meta="{meta}" data-delay="{i % 3}">
        <img src="assets/{img}" alt="{title}" loading="lazy">
        <div class="work-info"><span class="tag">{cat_label}</span><h3>{title}</h3><p>{meta.split('|')[0].strip()}</p></div>
      </article>"""
    return head("نمونه‌کارها", "گالری نمونه‌کارهای طراحی جلد و صفحه‌آرایی کتاب، مجله و کتاب کودک استودیو افرا گرافیک") + header() + page_hero("نمونه‌کارها", "نمونه‌کارهای ما", "گزیده‌ای از بیش از ۷۰۰ پروژه‌ی انجام‌شده. برای مشاهده‌ی جزئیات هر پروژه روی آن کلیک کنید.") + f"""
<section class="section--tight">
  <div class="container">
    <div class="filters">{filters()}</div>
    <div class="work-grid">{cards}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid-3">
      <div class="card reveal text-center"><span class="ic" style="display:inline-grid;place-items:center;width:56px;height:56px;border-radius:16px;background:var(--c-teal-light);color:var(--c-teal);margin-bottom:1rem">{ICONS["book"]}</span><h3>+۳۲۰ جلد</h3><p class="muted">در ژانرهای ادبی، کودک، دانشگاهی و عمومی</p></div>
      <div class="card reveal text-center" data-delay="1"><span class="ic" style="display:inline-grid;place-items:center;width:56px;height:56px;border-radius:16px;background:var(--c-terra-light);color:var(--c-terra);margin-bottom:1rem">{ICONS["layout"]}</span><h3>+۹۰٬۰۰۰ صفحه</h3><p class="muted">صفحه‌آرایی‌شده در ایندیزاین</p></div>
      <div class="card reveal text-center" data-delay="2"><span class="ic" style="display:inline-grid;place-items:center;width:56px;height:56px;border-radius:16px;background:var(--c-gold-light);color:#9d7a2a;margin-bottom:1rem">{ICONS["users"]}</span><h3>+۴۰ ناشر</h3><p class="muted">همکاری مستمر با انتشارات معتبر</p></div>
    </div>
  </div>
</section>
{cta_block()}
""" + footer()

# ======================================================
#  ثبت سفارش
# ======================================================
def order():
    def choice(val, icon, title, sub, checked=False):
        return f"""<label class="choice"><input type="radio" name="service" value="{val}" {"checked" if checked else ""}><span class="box">{ICONS[icon]}<b>{title}</b><small>{sub}</small></span></label>"""
    return head("ثبت سفارش", "ثبت آنلاین سفارش طراحی جلد و صفحه‌آرایی کتاب در چند مرحله ساده با برآورد فوری هزینه") + header() + page_hero("ثبت سفارش", "ثبت سفارش آنلاین", "در ۴ مرحله‌ی کوتاه مشخصات پروژه را وارد کنید. برآورد اولیه‌ی هزینه را همان لحظه می‌بینید و ظرف ۲۴ ساعت با شما تماس می‌گیریم.") + f"""
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
          <p class="muted">می‌توانید بعداً در جلسه‌ی مشاوره تغییرش دهید.</p>
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
          <div class="estimate"><div><small>برآورد اولیه‌ی هزینه</small><b id="estimate">—</b></div><small style="max-width:260px">این عدد تقریبی است و قیمت نهایی پس از بررسی فایل اعلام می‌شود.</small></div>
        </div>

        <!-- مرحله ۲ -->
        <div class="step-pane">
          <h3>مشخصات اثر</h3>
          <p class="muted">هرچه اطلاعات دقیق‌تر باشد، برآورد و طرح اولیه دقیق‌تر خواهد بود.</p>
          <div class="form-grid">
            <div class="field full"><label for="title">عنوان کتاب / نشریه <span class="req">*</span></label><input id="title" name="title" required placeholder="مثلاً: برگ‌های ارغوانی"><div class="err">عنوان را وارد کنید</div></div>
            <div class="field">
              <label for="genre">ژانر / موضوع <span class="req">*</span></label>
              <select id="genre" name="genre" required>
                <option value="">انتخاب کنید…</option><option>رمان و داستان</option><option>شعر</option><option>کودک و نوجوان</option><option>دانشگاهی و علمی</option><option>روان‌شناسی و توسعه فردی</option><option>تاریخ و دین</option><option>مجله و نشریه</option><option>سایر</option>
              </select><div class="err">ژانر را انتخاب کنید</div>
            </div>
            <div class="field">
              <label for="size">قطع کتاب</label>
              <select id="size" name="size"><option>رقعی (۱۴٫۵×۲۱٫۵)</option><option>وزیری (۱۷×۲۴)</option><option>رحلی (۲۱×۲۸)</option><option>خشتی (۲۱×۲۱)</option><option>پالتویی (۱۲×۲۱)</option><option>جیبی (۱۱×۱۷)</option><option>A4</option><option>سایر / نمی‌دانم</option></select>
            </div>
            <div class="field"><label for="author">نام نویسنده / ناشر</label><input id="author" name="author" placeholder="اختیاری"></div>
            <div class="field">
              <label for="binding">نوع جلد</label>
              <select id="binding" name="binding"><option>شومیز (نرم)</option><option>سخت (گالینگور)</option><option>سخت با روکش</option><option>نمی‌دانم — مشاوره می‌خواهم</option></select>
            </div>
            <div class="field full"><label for="brief">توضیحات و سلیقه‌ی شما</label><textarea id="brief" name="brief" placeholder="خلاصه‌ی اثر، حال‌وهوای مورد نظر، رنگ‌های محبوب، جلدهایی که دوست دارید یا ندارید، لینک نمونه‌های الهام‌بخش…"></textarea></div>
            <div class="field full">
              <label>فایل‌ها <span class="opt">(اختیاری — فایل متن، تصاویر، نمونه‌های الهام‌بخش)</span></label>
              <div class="upload">{ICONS["upload"]}<b>فایل را این‌جا رها کنید یا کلیک کنید</b><p class="muted" style="margin:.3rem 0 0;font-size:.85rem">Word، PDF، تصویر — حداکثر ۵۰ مگابایت</p><input type="file" multiple></div>
              <ul class="upload-list"></ul>
            </div>
          </div>
        </div>

        <!-- مرحله ۳ -->
        <div class="step-pane">
          <h3>اطلاعات تماس</h3>
          <p class="muted">برای هماهنگی و ارسال پیش‌نمایش‌ها از این اطلاعات استفاده می‌کنیم.</p>
          <div class="form-grid">
            <div class="field"><label for="name">نام و نام خانوادگی <span class="req">*</span></label><input id="name" name="name" required placeholder="نام شما"><div class="err">نام را وارد کنید</div></div>
            <div class="field"><label for="phone">شماره موبایل <span class="req">*</span></label><input id="phone" name="phone" type="tel" required placeholder="09xx xxx xxxx" style="direction:ltr;text-align:right"><div class="err">شماره موبایل معتبر وارد کنید</div></div>
            <div class="field"><label for="email">ایمیل <span class="opt">(اختیاری)</span></label><input id="email" name="email" type="email" placeholder="you@example.com" style="direction:ltr;text-align:right"><div class="err">ایمیل معتبر وارد کنید</div></div>
            <div class="field">
              <label for="contactvia">روش ارتباط ترجیحی</label>
              <select id="contactvia" name="contactvia"><option>تماس تلفنی</option><option>واتساپ</option><option>تلگرام</option><option>ایمیل</option></select>
            </div>
            <div class="field full">
              <label for="role">شما…</label>
              <select id="role" name="role"><option>نویسنده‌ی مستقل هستم</option><option>از طرف انتشارات هستم</option><option>مترجم هستم</option><option>سازمان / شرکت هستم</option></select>
            </div>
          </div>
        </div>

        <!-- مرحله ۴ -->
        <div class="step-pane">
          <h3>بازبینی و ارسال</h3>
          <p class="muted">لطفاً اطلاعات را بررسی کنید. پس از ارسال، کد پیگیری دریافت می‌کنید.</p>
          <div class="summary"><dl id="summary"></dl></div>
          <div class="field" style="margin-top:1.25rem">
            <label style="display:flex;gap:.6rem;align-items:flex-start;font-weight:500;font-size:.92rem;cursor:pointer"><input type="checkbox" name="agree" required style="width:18px;height:18px;margin-top:.3rem;accent-color:var(--c-teal)"><span><a href="#" style="color:var(--c-teal)">شرایط همکاری</a> را مطالعه کرده‌ام و می‌پذیرم. اطلاعات و فایل‌های من محرمانه باقی می‌ماند.</span></label>
            <div class="err">برای ادامه باید شرایط را بپذیرید</div>
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
      <h2>سفارش شما ثبت شد 🎉</h2>
      <p>ممنون از اعتمادتان. کد پیگیری شما:</p>
      <div class="code">AF-000000</div>
      <p class="muted">همکاران ما ظرف ۲۴ ساعت کاری برای هماهنگی جزئیات و اعلام قیمت نهایی با شما تماس می‌گیرند. پیامک تأیید نیز برای‌تان ارسال شد.</p>
      <div style="display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap;margin-top:1.5rem">
        <a href="index.html" class="btn btn-outline">بازگشت به خانه</a>
        <a href="consult.html" class="btn btn-primary">رزرو جلسه‌ی مشاوره</a>
      </div>
    </div>

    <aside class="sticky">
      <div class="side-card">
        <h3>بعد از ثبت سفارش چه می‌شود؟</h3>
        <ul class="timeline">
          <li><small>تا ۲۴ ساعت</small><b>تماس هماهنگی</b><p>جزئیات را نهایی و قیمت دقیق را اعلام می‌کنیم.</p></li>
          <li><small>پس از تأیید</small><b>قرارداد و پیش‌پرداخت</b><p>۴۰٪ پیش‌پرداخت، مابقی پس از تأیید نهایی.</p></li>
          <li><small>۴۸ ساعت بعد</small><b>اتود اولیه</b><p>اولین طرح‌ها یا نمونه‌ی چند صفحه را می‌بینید.</p></li>
          <li><small>پایان پروژه</small><b>تحویل فایل‌ها</b><p>PDF چاپ، فایل باز و نسخه‌ی دیجیتال.</p></li>
        </ul>
      </div>
      <div class="side-card">
        <h3>نیاز به راهنمایی دارید؟</h3>
        <p style="font-size:.92rem">اگر ترجیح می‌دهید قبل از ثبت سفارش صحبت کنیم:</p>
        <a href="consult.html" class="btn btn-outline btn-block" style="margin-bottom:.6rem">رزرو مشاوره رایگان</a>
        <a href="https://wa.me/989120000000" class="btn btn-block" style="background:#25d366;color:#fff">{ICONS["wa"]} گفتگو در واتساپ</a>
      </div>
    </aside>
  </div>
</section>
""" + footer()

# ======================================================
#  مشاوره
# ======================================================
def consult():
    return head("مشاوره رایگان", "رزرو جلسه مشاوره رایگان ۲۰ دقیقه‌ای برای طراحی جلد و صفحه‌آرایی کتاب با افرا حسین‌زاده") + header() + page_hero("مشاوره", "مشاوره‌ی رایگان ۲۰ دقیقه‌ای", "درباره‌ی کتاب‌تان، مسیر چاپ، هزینه‌ها و انتخاب سبک صفحه‌آرایی صحبت می‌کنیم — بدون هیچ تعهدی.") + f"""
<section class="section--tight">
  <div class="container two-col">
    <div id="consult-wrap">
      <form id="consult-form" class="form-card" novalidate>
        <h3>۱. روز و ساعت را انتخاب کنید</h3>
        <p class="muted" style="font-size:.9rem">ساعات به وقت تهران است. جمعه‌ها تعطیل هستیم.</p>
        <div class="days" style="margin-bottom:1.25rem"></div>
        <div class="slots"></div>
        <input type="hidden" id="sel-date" name="date"><input type="hidden" id="sel-time" name="time">

        <div class="divider"></div>
        <h3>۲. نوع جلسه</h3>
        <div class="field" data-required-group>
          <div class="choice-grid">
            <label class="choice"><input type="radio" name="type" value="call" checked><span class="box">{ICONS["phone"]}<b>تماس تلفنی</b><small>ساده و سریع</small></span></label>
            <label class="choice"><input type="radio" name="type" value="video"><span class="box">{ICONS["video"]}<b>تماس تصویری</b><small>Google Meet / اسکایپ</small></span></label>
            <label class="choice"><input type="radio" name="type" value="chat"><span class="box">{ICONS["chat"]}<b>چت واتساپ</b><small>پاسخ مکتوب</small></span></label>
          </div>
        </div>

        <div class="divider"></div>
        <h3>۳. اطلاعات شما</h3>
        <div class="form-grid">
          <div class="field"><label for="cname">نام و نام خانوادگی <span class="req">*</span></label><input id="cname" name="name" required><div class="err">نام را وارد کنید</div></div>
          <div class="field"><label for="cphone">شماره موبایل <span class="req">*</span></label><input id="cphone" name="phone" type="tel" required placeholder="09xx xxx xxxx" style="direction:ltr;text-align:right"><div class="err">شماره موبایل معتبر وارد کنید</div></div>
          <div class="field full">
            <label for="ctopic">موضوع مشاوره <span class="req">*</span></label>
            <select id="ctopic" name="topic" required>
              <option value="">انتخاب کنید…</option>
              <option>می‌خواهم اولین کتابم را چاپ کنم و نمی‌دانم از کجا شروع کنم</option>
              <option>برآورد هزینه و زمان پروژه</option>
              <option>انتخاب سبک جلد و صفحه‌آرایی</option>
              <option>همکاری بلندمدت انتشارات</option>
              <option>مشکل فنی در فایل فعلی</option>
              <option>سایر</option>
            </select><div class="err">موضوع را انتخاب کنید</div>
          </div>
          <div class="field full"><label for="cnote">توضیح کوتاه <span class="opt">(اختیاری)</span></label><textarea id="cnote" name="note" style="min-height:100px" placeholder="هرچه بیشتر بدانیم، جلسه مفیدتر خواهد بود…"></textarea></div>
        </div>
        <div style="margin-top:1.5rem"><button type="submit" class="btn btn-primary btn-lg btn-block">تأیید و رزرو جلسه</button></div>
      </form>
    </div>

    <div id="consult-success" class="form-card success hidden">
      <div class="ok">{ICONS["check"]}</div>
      <h2>جلسه‌ی شما رزرو شد ✅</h2>
      <p>زمان جلسه:</p>
      <div class="code" data-when>—</div>
      <p class="muted">پیامک یادآوری یک ساعت قبل از جلسه برای‌تان ارسال می‌شود. اگر نیاز به تغییر زمان داشتید، کافی است به همان پیامک پاسخ دهید.</p>
      <div style="display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap;margin-top:1.5rem">
        <a href="portfolio.html" class="btn btn-outline">تا آن موقع نمونه‌کارها را ببینید</a>
        <a href="index.html" class="btn btn-primary">بازگشت به خانه</a>
      </div>
    </div>

    <aside class="sticky">
      <div class="side-card">
        <h3>در این جلسه چه می‌گذرد؟</h3>
        <ul class="check-list">
          <li>{ICONS["check"]}آشنایی با کتاب و هدف شما از انتشار</li>
          <li>{ICONS["check"]}راهنمایی درباره‌ی قطع، کاغذ و نوع جلد</li>
          <li>{ICONS["check"]}برآورد شفاف هزینه و زمان</li>
          <li>{ICONS["check"]}مسیر شابک، فیپا و همکاری با ناشر</li>
          <li>{ICONS["check"]}پاسخ به همه‌ی سؤال‌های شما</li>
        </ul>
      </div>
      <div class="side-card" style="display:flex;gap:1rem;align-items:center">
        <img src="assets/designer.jpg" alt="افرا حسین‌زاده" style="width:64px;height:64px;border-radius:50%;object-fit:cover;flex-shrink:0">
        <div><b>افرا حسین‌زاده</b><p style="margin:0;font-size:.85rem">طراح جلد و صفحه‌آرا — ۱۰+ سال تجربه</p></div>
      </div>
      <div class="side-card">
        <h3>ترجیح می‌دهید فوری صحبت کنیم؟</h3>
        <a href="tel:+989120000000" class="btn btn-outline btn-block" style="margin-bottom:.6rem">{ICONS["phone"]} <span dir="ltr">0912 000 0000</span></a>
        <a href="https://wa.me/989120000000" class="btn btn-block" style="background:#25d366;color:#fff">{ICONS["wa"]} واتساپ</a>
      </div>
    </aside>
  </div>
</section>
""" + footer()

# ======================================================
#  درباره
# ======================================================
def about():
    return head("درباره افرا", "آشنایی با افرا حسین‌زاده و تیم استودیو افرا گرافیک؛ بیش از ده سال تجربه در طراحی جلد و صفحه‌آرایی کتاب") + header() + page_hero("درباره افرا", "درباره‌ی افرا گرافیک", "استودیویی کوچک با عشق بزرگ به کتاب. ما کلمات را به شکل درمی‌آوریم.") + f"""
<section class="section--tight">
  <div class="container about-grid">
    <div class="about-img reveal">
      <img src="assets/designer.jpg" alt="افرا حسین‌زاده">
      <div class="exp-badge"><b>۱۰+</b><small>سال تجربه</small></div>
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">داستان ما</span>
      <h2>سلام، من افرا حسین‌زاده هستم</h2>
      <p>بیش از ده سال است که در حوزه‌ی طراحی جلد و صفحه‌آرایی کتاب و مجله فعالیت می‌کنم. با ناشران زیادی همکاری داشته‌ام و رزومه‌ی مفصلی در این حوزه دارم. عاشق صفحه‌آرایی‌ام و عاشق کتاب خواندن؛ به نظرم لذت‌بخش‌ترین کار دنیا، کار کردن با کلمات است.</p>
      <p>چند سال پیش تیم طراحی‌ای شکل دادیم و تصمیم گرفتیم فعالیت‌مان را گسترده‌تر کنیم تا علاوه بر ناشران، نویسندگان مستقل هم به کیفیتی حرفه‌ای و قیمتی منصفانه دسترسی داشته باشند. باور ما این است که هر کتاب خوبی، شایسته‌ی یک جلد و صفحه‌آرایی خوب است.</p>
      <div class="mini-stats">
        <div><b>+۴۵۰</b><span>کتاب</span></div>
        <div><b>+۴۰</b><span>ناشر همکار</span></div>
        <div><b>۹۸٪</b><span>رضایت</span></div>
      </div>
      <div class="tools" style="margin-top:2rem"><span>Adobe InDesign</span><span>Photoshop</span><span>Illustrator</span><span>Affinity Publisher</span><span>Figma</span><span>Procreate</span></div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="container">
    <div class="sec-head center"><span class="eyebrow">ارزش‌های ما</span><h2>چرا ناشران به ما اعتماد می‌کنند؟</h2></div>
    <div class="grid-3">
      <div class="card reveal"><span class="ic" style="display:inline-grid;place-items:center;width:52px;height:52px;border-radius:14px;background:var(--c-teal-light);color:var(--c-teal);margin-bottom:1rem">{ICONS["shield"]}</span><h3>دقت در جزئیات</h3><p>نیم‌فاصله، کشیدگی، یتیم و بیوه… ما به همان چیزهایی اهمیت می‌دهیم که خواننده ناخودآگاه حس می‌کند.</p></div>
      <div class="card reveal" data-delay="1"><span class="ic" style="display:inline-grid;place-items:center;width:52px;height:52px;border-radius:14px;background:var(--c-terra-light);color:var(--c-terra);margin-bottom:1rem">{ICONS["clock"]}</span><h3>تعهد به زمان</h3><p>زمان‌بندی مشخص در قرارداد؛ بیش از ۹۵٪ پروژه‌ها را زودتر از موعد تحویل داده‌ایم.</p></div>
      <div class="card reveal" data-delay="2"><span class="ic" style="display:inline-grid;place-items:center;width:52px;height:52px;border-radius:14px;background:var(--c-gold-light);color:#9d7a2a;margin-bottom:1rem">{ICONS["chat"]}</span><h3>ارتباط شفاف</h3><p>در هر مرحله می‌دانید کار کجاست. بدون هزینه‌ی پنهان، بدون غافلگیری.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container two-col" style="grid-template-columns:1fr 1fr">
    <div>
      <span class="eyebrow">مسیر ما</span>
      <h2>از یک میز کوچک تا یک تیم</h2>
      <ul class="timeline" style="margin-top:1.5rem">
        <li><small>۱۳۹۲</small><b>شروع کار</b><p>اولین صفحه‌آرایی برای یک ناشر کوچک در تهران.</p></li>
        <li><small>۱۳۹۵</small><b>همکاری با ناشران بزرگ</b><p>آغاز همکاری مستمر با چند انتشارات معتبر.</p></li>
        <li><small>۱۳۹۹</small><b>شکل‌گیری تیم</b><p>پیوستن تصویرگر و ویراستار به تیم افرا.</p></li>
        <li><small>۱۴۰۲</small><b>افرا گرافیک</b><p>راه‌اندازی استودیو و خدمات آنلاین برای نویسندگان مستقل.</p></li>
        <li><small>امروز</small><b>+۴۵۰ کتاب</b><p>و هنوز هر کتاب تازه برای‌مان هیجان‌انگیز است.</p></li>
      </ul>
    </div>
    <div>
      <span class="eyebrow">تیم</span>
      <h2>کسانی که کتاب شما را می‌سازند</h2>
      <div style="display:grid;gap:1rem;margin-top:1.5rem">
        <div class="card" style="display:flex;gap:1rem;align-items:center;padding:1.2rem"><span class="av" style="width:56px;height:56px;border-radius:16px;background:var(--c-teal);color:#fff;display:grid;place-items:center;font-weight:900;font-size:1.3rem;flex-shrink:0">ا</span><div><b>افرا حسین‌زاده</b><p style="margin:0;font-size:.88rem">مدیر هنری، طراح جلد و صفحه‌آرا</p></div></div>
        <div class="card" style="display:flex;gap:1rem;align-items:center;padding:1.2rem"><span class="av" style="width:56px;height:56px;border-radius:16px;background:var(--c-terra);color:#fff;display:grid;place-items:center;font-weight:900;font-size:1.3rem;flex-shrink:0">ن</span><div><b>نگار امینی</b><p style="margin:0;font-size:.88rem">تصویرگر و طراح گرافیک</p></div></div>
        <div class="card" style="display:flex;gap:1rem;align-items:center;padding:1.2rem"><span class="av" style="width:56px;height:56px;border-radius:16px;background:var(--c-gold);color:#fff;display:grid;place-items:center;font-weight:900;font-size:1.3rem;flex-shrink:0">ر</span><div><b>رضا صادقی</b><p style="margin:0;font-size:.88rem">ویراستار و نمونه‌خوان</p></div></div>
        <div class="card" style="display:flex;gap:1rem;align-items:center;padding:1.2rem"><span class="av" style="width:56px;height:56px;border-radius:16px;background:var(--c-ink-2);color:#fff;display:grid;place-items:center;font-weight:900;font-size:1.3rem;flex-shrink:0">م</span><div><b>مینا کاظمی</b><p style="margin:0;font-size:.88rem">مدیر پروژه و ارتباط با مشتری</p></div></div>
      </div>
    </div>
  </div>
</section>
{cta_block()}
""" + footer()

# ======================================================
#  بلاگ
# ======================================================
def blog():
    posts = [
        ("layout-1.jpg", "آموزش", "۱۰ اشتباه رایج در صفحه‌آرایی کتاب فارسی", "از کشیدگی‌های نابه‌جا تا فاصله‌ی خطوط اشتباه؛ اشتباهاتی که خوانایی کتاب را از بین می‌برند.", "۷ دقیقه", "۱۲ شهریور ۱۴۰۴"),
        ("cover-1.jpg", "طراحی جلد", "جلد کتاب چطور فروش را تغییر می‌دهد؟", "خواننده در ۳ ثانیه تصمیم می‌گیرد کتاب را بردارد یا نه. جلد، اولین و مهم‌ترین تبلیغ کتاب شماست.", "۵ دقیقه", "۲ شهریور ۱۴۰۴"),
        ("cover-4.jpg", "راهنمای نشر", "راهنمای کامل چاپ اولین کتاب برای نویسندگان مستقل", "از ویرایش و شابک تا انتخاب چاپخانه؛ همه‌ی مراحلی که باید بدانید.", "۱۲ دقیقه", "۲۰ مرداد ۱۴۰۴"),
        ("layout-2.jpg", "آموزش", "انتخاب فونت مناسب برای متن کتاب فارسی", "مقایسه‌ی فونت‌های پرکاربرد متن (ایران‌سنس، وزیر، نازنین، میترا) و توصیه‌ها بر اساس ژانر.", "۸ دقیقه", "۵ مرداد ۱۴۰۴"),
        ("cover-3.jpg", "کتاب کودک", "اصول طراحی کتاب کودک: رنگ، فونت و ریتم صفحه", "چرا کتاب کودک با هر کتاب دیگری فرق دارد و چه چیزهایی را باید رعایت کرد.", "۶ دقیقه", "۱۸ تیر ۱۴۰۴"),
        ("cover-2.jpg", "راهنمای نشر", "قطع کتاب: رقعی، وزیری یا پالتویی؟", "راهنمای انتخاب قطع بر اساس ژانر، حجم و بودجه‌ی چاپ.", "۴ دقیقه", "۳ تیر ۱۴۰۴"),
    ]
    cards = ""
    for i, (img, cat, title, desc, rt, date) in enumerate(posts):
        cards += f"""
      <article class="post reveal" data-delay="{i % 3}">
        <a href="#"><img src="assets/{img}" alt="{title}" loading="lazy"></a>
        <div class="body">
          <span class="cat">{cat}</span>
          <h3><a href="#">{title}</a></h3>
          <p>{desc}</p>
          <div class="foot"><span>{date}</span><span>{rt} مطالعه</span></div>
        </div>
      </article>"""
    return head("مجله", "مقالات آموزشی درباره طراحی جلد، صفحه‌آرایی، تایپوگرافی فارسی و راهنمای چاپ کتاب") + header() + page_hero("مجله", "مجله‌ی افرا", "نکات کاربردی درباره‌ی طراحی جلد، صفحه‌آرایی و مسیر نشر — برای نویسندگان، مترجمان و ناشران.") + f"""
<section class="section--tight">
  <div class="container">
    <div class="filters"><button class="filter-btn active">همه</button><button class="filter-btn">آموزش</button><button class="filter-btn">طراحی جلد</button><button class="filter-btn">راهنمای نشر</button><button class="filter-btn">کتاب کودک</button></div>
    <div class="blog-grid">{cards}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="cta reveal" style="text-align:right;display:grid;grid-template-columns:1.2fr 1fr;gap:2rem;align-items:center">
      <div><h2 style="font-size:1.7rem">خبرنامه‌ی ماهانه‌ی افرا</h2><p style="margin:0">هر ماه یک مقاله‌ی کاربردی و پشت‌صحنه‌ی یک پروژه. بدون اسپم.</p></div>
      <form data-simple="عضویت شما در خبرنامه ثبت شد ✅" style="display:flex;gap:.6rem;position:relative;flex-wrap:wrap">
        <div class="field" style="flex:1;min-width:200px"><input type="email" required placeholder="ایمیل شما" style="direction:ltr;text-align:right;background:#fff;border-color:transparent;color:#1c2226"></div>
        <button type="submit" class="btn btn-primary" style="background:#fff;color:var(--c-teal-dark)">عضویت</button>
      </form>
    </div>
  </div>
</section>
""" + footer()

# ======================================================
#  تماس
# ======================================================
def contact():
    return head("تماس با ما", "راه‌های ارتباط با استودیو افرا گرافیک؛ تلفن، واتساپ، ایمیل و فرم تماس") + header() + page_hero("تماس", "تماس با ما", "خوشحال می‌شویم درباره‌ی کتاب‌تان بشنویم. از هر راهی که راحت‌ترید پیام بدهید.") + f"""
<section class="section--tight">
  <div class="container">
    <div class="contact-cards">
      <a href="tel:+989120000000" class="ccard reveal"><span class="ic">{ICONS["phone"]}</span><b>تلفن و واتساپ</b><span>0912 000 0000</span></a>
      <a href="mailto:info@afradesigner.ir" class="ccard reveal" data-delay="1"><span class="ic" style="background:var(--c-terra-light);color:var(--c-terra)">{ICONS["mail"]}</span><b>ایمیل</b><span>info@afradesigner.ir</span></a>
      <div class="ccard reveal" data-delay="2"><span class="ic" style="background:var(--c-gold-light);color:#9d7a2a">{ICONS["clock"]}</span><b>ساعات پاسخگویی</b><span style="direction:rtl">شنبه تا پنج‌شنبه، ۱۰ تا ۱۸</span></div>
    </div>
    <div class="two-col" style="grid-template-columns:1.2fr 1fr">
      <form class="form-card" data-simple="پیام شما ارسال شد؛ به‌زودی پاسخ می‌دهیم ✅" novalidate>
        <h3>فرم تماس</h3>
        <p class="muted" style="font-size:.92rem">معمولاً ظرف چند ساعت کاری پاسخ می‌دهیم.</p>
        <div class="form-grid">
          <div class="field"><label>نام <span class="req">*</span></label><input name="name" required><div class="err">نام را وارد کنید</div></div>
          <div class="field"><label>موبایل یا ایمیل <span class="req">*</span></label><input name="contact" required style="direction:ltr;text-align:right"><div class="err">راه ارتباطی را وارد کنید</div></div>
          <div class="field full"><label>موضوع</label><select name="subject"><option>سؤال درباره‌ی خدمات</option><option>پیگیری سفارش</option><option>همکاری انتشارات</option><option>همکاری به عنوان طراح</option><option>سایر</option></select></div>
          <div class="field full"><label>پیام <span class="req">*</span></label><textarea name="message" required></textarea><div class="err">پیام را وارد کنید</div></div>
        </div>
        <div style="margin-top:1.25rem"><button type="submit" class="btn btn-primary btn-lg">ارسال پیام</button></div>
      </form>
      <div>
        <div class="side-card">
          <h3>ما را دنبال کنید</h3>
          <p style="font-size:.92rem">پشت‌صحنه‌ی پروژه‌ها و نکات طراحی را در شبکه‌های اجتماعی منتشر می‌کنیم.</p>
          <div class="socials" style="margin-top:.5rem">
            <a href="#" aria-label="اینستاگرام" style="background:var(--c-surface-2);color:var(--c-ink)">{ICONS["ig"]}</a>
            <a href="#" aria-label="تلگرام" style="background:var(--c-surface-2);color:var(--c-ink)">{ICONS["tg"]}</a>
            <a href="#" aria-label="واتساپ" style="background:var(--c-surface-2);color:var(--c-ink)">{ICONS["wa"]}</a>
            <a href="#" aria-label="لینکدین" style="background:var(--c-surface-2);color:var(--c-ink)">{ICONS["linkedin"]}</a>
          </div>
        </div>
        <div class="side-card">
          <h3>همکاری آنلاین با سراسر ایران</h3>
          <p style="font-size:.92rem;margin:0">تمام مراحل کار — از بریف تا تحویل — به صورت آنلاین انجام می‌شود. برای ناشران تهران امکان جلسه‌ی حضوری نیز وجود دارد.</p>
        </div>
        <div class="map-box" style="margin-top:1.25rem">
          <div class="text-center" style="padding:1rem">{ICONS["pin"].replace('viewBox', 'width="40" height="40" viewBox')}<p style="margin:.5rem 0 0">تهران — جلسه‌ی حضوری با هماهنگی قبلی</p></div>
        </div>
      </div>
    </div>
  </div>
</section>
{cta_block()}
""" + footer()

PAGES = {
    "index.html": index, "services.html": services, "portfolio.html": portfolio,
    "order.html": order, "consult.html": consult, "about.html": about,
    "blog.html": blog, "contact.html": contact,
}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in PAGES.items():
        with open(os.path.join(here, name), "w", encoding="utf-8") as f:
            f.write(fn())
        print("✓", name)
