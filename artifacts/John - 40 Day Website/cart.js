/* cart.js — shared navigation + cart for 40daycampaigns.com
   Injected on every page. Safe storage (localStorage with in-memory fallback). */
(function(){
  /* ---------- safe storage ---------- */
  var MEM = {};
  function sGet(k){ try{ return localStorage.getItem(k); }catch(e){ return MEM[k]||null; } }
  function sSet(k,v){ try{ localStorage.setItem(k,v); }catch(e){ MEM[k]=v; } }
  function cart(){ try{ return JSON.parse(sGet('ltCart')||'[]'); }catch(e){ return []; } }
  function save(c){ sSet('ltCart', JSON.stringify(c)); paint(); }
  function user(){ try{ return JSON.parse(sGet('ltUser')||'null'); }catch(e){ return null; } }

  /* ---------- catalog lookup (data.js may not be loaded on every page) ---------- */
  function row(id){ return (window.CAMPAIGNS||[]).find(function(r){ return r[9]===id; }); }

  /* ---------- styles ---------- */
  var css = ''+
  '.ltnav{position:sticky;top:0;z-index:900;background:rgba(255,255,255,.94);backdrop-filter:blur(10px);border-bottom:1px solid #EAE7F0;font-family:\'Hanken Grotesk\',sans-serif}'+
  '.ltnav .in{max-width:1240px;margin:0 auto;display:flex;align-items:center;gap:26px;padding:14px 28px}'+
  '.ltnav .logo{font-weight:900;font-size:17px;letter-spacing:-.2px;color:#16161D;text-decoration:none;white-space:nowrap}'+
  '.ltnav .logo b{color:#F26C1E}'+
  '.ltnav .lk{color:#3A3A45;text-decoration:none;font-weight:600;font-size:14.5px;padding:6px 2px}'+
  '.ltnav .lk:hover,.ltnav .lk.on{color:#16161D}'+
  '.ltnav .lk.on{box-shadow:inset 0 -2px 0 #F26C1E}'+
  '.ltnav .sp{flex:1}'+
  '.ltnav .cta{background:#16161D;color:#fff;border-radius:999px;padding:9px 16px;font-weight:700;font-size:13.5px;text-decoration:none;white-space:nowrap}'+
  '.ltnav .cta:hover{background:#000}'+
  '.ltnav .cartb{position:relative;border:1px solid #EAE7F0;background:#fff;border-radius:999px;width:38px;height:38px;display:flex;align-items:center;justify-content:center;cursor:pointer}'+
  '.ltnav .cartb .n{position:absolute;top:-5px;right:-5px;background:#F26C1E;color:#fff;font-size:10.5px;font-weight:800;border-radius:999px;min-width:17px;height:17px;display:flex;align-items:center;justify-content:center;padding:0 4px}'+
  '.ltnav .burger{display:none;border:0;background:none;cursor:pointer;padding:6px}'+
  '@media(max-width:960px){.ltnav .lk,.ltnav .cta{display:none}.ltnav .burger{display:block}.ltnav.open .menu{display:flex}}'+
  '.ltnav .menu{display:contents}'+
  '@media(max-width:960px){.ltnav .menu{display:none;position:absolute;top:100%;left:0;right:0;background:#fff;border-bottom:1px solid #EAE7F0;flex-direction:column;padding:12px 28px;gap:4px}.ltnav.open .menu .lk,.ltnav.open .menu .cta{display:block;padding:10px 0}}'+
  '.ltdrawer{position:fixed;inset:0;z-index:950;display:none}'+
  '.ltdrawer.open{display:block}'+
  '.ltdrawer .bg{position:absolute;inset:0;background:rgba(22,22,29,.42)}'+
  '.ltdrawer .panel{position:absolute;top:0;right:0;bottom:0;width:min(400px,92vw);background:#fff;box-shadow:-18px 0 50px rgba(22,22,29,.18);display:flex;flex-direction:column;font-family:\'Hanken Grotesk\',sans-serif}'+
  '.ltdrawer h4{margin:0;padding:20px 22px;border-bottom:1px solid #EAE7F0;font-size:16px;color:#16161D;display:flex;justify-content:space-between;align-items:center}'+
  '.ltdrawer .x{border:0;background:none;font-size:20px;cursor:pointer;color:#5E5E6B;line-height:1}'+
  '.ltdrawer .items{flex:1;overflow:auto;padding:14px 22px}'+
  '.ltdrawer .it{display:flex;justify-content:space-between;gap:12px;padding:12px 0;border-bottom:1px solid #F4F2F8}'+
  '.ltdrawer .it .t{font-weight:700;font-size:14px;color:#16161D}'+
  '.ltdrawer .it .s{font-size:12.5px;color:#5E5E6B;margin-top:2px}'+
  '.ltdrawer .it .rm{border:0;background:none;color:#8A8A98;cursor:pointer;font-size:12.5px;text-decoration:underline;padding:0}'+
  '.ltdrawer .it .pr{font-weight:800;color:#16161D;white-space:nowrap}'+
  '.ltdrawer .empty{color:#5E5E6B;font-size:14px;padding:26px 0;text-align:center}'+
  '.ltdrawer .foot{border-top:1px solid #EAE7F0;padding:18px 22px}'+
  '.ltdrawer .tot{display:flex;justify-content:space-between;font-weight:800;color:#16161D;margin-bottom:12px}'+
  '.ltdrawer .go{display:block;text-align:center;background:#F26C1E;color:#fff;border-radius:999px;padding:12px;font-weight:800;text-decoration:none}'+
  '.ltdrawer .note{font-size:11.5px;color:#8A8A98;text-align:center;margin-top:9px}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  /* ---------- nav ---------- */
  var here = (location.pathname.split('/').pop()||'index.html');
  function on(f){ return here===f ? ' on' : ''; }
  var u = user();
  var hasOwnNav = !!document.querySelector('.navwrap');
  var nav = document.createElement('nav'); nav.className='ltnav';
  nav.innerHTML = '<div class="in">'+
    '<a class="logo" href="index.html">40 DAY <b>CAMPAIGNS</b></a>'+
    '<div class="menu">'+
    '<a class="lk'+on('browse.html')+'" href="browse.html">Campaigns</a>'+
    '<a class="lk'+on('finder.html')+'" href="finder.html">Campaign Finder</a>'+
    '<a class="lk'+on('how-it-works.html')+'" href="how-it-works.html">How it works</a>'+
    '<a class="lk'+on('pricing.html')+'" href="pricing.html">Pricing</a>'+
    '<a class="lk'+on('sample.html')+'" href="sample.html">Sample</a>'+
    '<span class="sp"></span>'+
    (u ? '<a class="lk" href="confirmation.html">Hi, '+(u.name||'friend').split(' ')[0]+'</a>'
       : '<a class="lk'+on('signin.html')+'" href="signin.html">Sign in</a>')+
    '<a class="cta" href="get-access.html">Get All Access</a>'+
    '</div>'+
    '<button class="cartb" id="ltCartBtn" aria-label="Cart"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#16161D" stroke-width="2"><circle cx="9" cy="21" r="1.6"/><circle cx="19" cy="21" r="1.6"/><path d="M2.5 3h3l2.4 12.3a2 2 0 0 0 2 1.7h7.7a2 2 0 0 0 2-1.6L21.5 7H6.2"/></svg><span class="n" id="ltCartN" style="display:none">0</span></button>'+
    '<button class="burger" id="ltBurger" aria-label="Menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#16161D" stroke-width="2.4"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>'+
    '</div>';
  if(!hasOwnNav){
    document.body.insertBefore(nav, document.body.firstChild);
    document.getElementById('ltBurger').addEventListener('click', function(){ nav.classList.toggle('open'); });
  } else {
    /* page has its own nav — just add the cart button into it */
    var host = document.querySelector('.navwrap .nright') || document.querySelector('.navwrap .nav') || document.querySelector('.navwrap');
    var cb = document.createElement('button');
    cb.className = 'cartb'; cb.id = 'ltCartBtn'; cb.setAttribute('aria-label','Cart');
    cb.style.cssText = 'position:relative;border:1px solid #EAE7F0;background:#fff;border-radius:999px;width:38px;height:38px;display:inline-flex;align-items:center;justify-content:center;cursor:pointer;margin-left:10px;vertical-align:middle;flex:none';
    cb.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#16161D" stroke-width="2"><circle cx="9" cy="21" r="1.6"/><circle cx="19" cy="21" r="1.6"/><path d="M2.5 3h3l2.4 12.3a2 2 0 0 0 2 1.7h7.7a2 2 0 0 0 2-1.6L21.5 7H6.2"/></svg><span class="n" id="ltCartN" style="display:none;position:absolute;top:-5px;right:-5px;background:#F26C1E;color:#fff;font-size:10.5px;font-weight:800;border-radius:999px;min-width:17px;height:17px;align-items:center;justify-content:center;padding:0 4px">0</span>';
    host.appendChild(cb);
  }

  /* ---------- drawer ---------- */
  var dr = document.createElement('div'); dr.className='ltdrawer';
  dr.innerHTML = '<div class="bg"></div><div class="panel">'+
    '<h4>Your cart <button class="x" aria-label="Close">×</button></h4>'+
    '<div class="items" id="ltItems"></div>'+
    '<div class="foot"><div class="tot"><span>Subtotal</span><span id="ltTot">$0</span></div>'+
    '<a class="go" href="get-access.html">Checkout</a>'+
    '<div class="note">Demo checkout — no payment is processed yet.</div></div></div>';
  document.body.appendChild(dr);
  dr.querySelector('.bg').addEventListener('click', function(){ dr.classList.remove('open'); });
  dr.querySelector('.x').addEventListener('click', function(){ dr.classList.remove('open'); });
  document.getElementById('ltCartBtn').addEventListener('click', function(){ dr.classList.add('open'); paint(); });

  /* ---------- paint ---------- */
  function paint(){
    var c = cart(), n = document.getElementById('ltCartN'), box = document.getElementById('ltItems');
    n.style.display = c.length ? 'flex':'none'; n.textContent = c.length;
    if(!box) return;
    if(!c.length){ box.innerHTML = '<div class="empty">Your cart is empty.<br>Every campaign is $199, or get everything with All&nbsp;Access.</div>'; }
    else {
      box.innerHTML = c.map(function(it,i){
        return '<div class="it"><div><div class="t">'+it.title+'</div><div class="s">'+(it.sub||it.fmt||'Complete campaign')+'</div>'+
        '<button class="rm" data-i="'+i+'">Remove</button></div><div class="pr">$'+it.price+'</div></div>';
      }).join('');
      box.querySelectorAll('.rm').forEach(function(b){
        b.addEventListener('click', function(){ var c2=cart(); c2.splice(+b.dataset.i,1); save(c2); });
      });
    }
    var tot = c.reduce(function(a,x){ return a + (x.price||199); }, 0);
    var tl = document.getElementById('ltTot'); if(tl) tl.textContent = '$'+tot;
  }

  /* ---------- public API ---------- */
  window.CART_ADD = function(id, title, sub, fmt){
    var r = row(id);
    var c = cart();
    if(c.some(function(x){ return x.id===id; })){ dr.classList.add('open'); paint(); return; }
    c.push({ id:id, title:title||(r?r[0]:id), sub:sub||(r?r[1]:''), fmt:fmt||(r?r[3]:''), price:199 });
    save(c); dr.classList.add('open');
  };
  window.CART_COUNT = function(){ return cart().length; };
  paint();
})();
