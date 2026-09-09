/* Lifetogether cart + accounts (browser-local; syncs to cloud at platform launch) */
(function(){
'use strict';
const LT={
 PRICE:199,
 cart(){try{return JSON.parse(localStorage.getItem('lt_cart')||'[]');}catch(e){return[];}},
 saveCart(c){localStorage.setItem('lt_cart',JSON.stringify(c));LT.badge();},
 add(id,fmt){const c=LT.cart();const ex=c.find(x=>x.id===id&&x.fmt===fmt);
   if(ex)ex.qty=Math.min(99,(ex.qty||1)+0);else c.push({id,fmt,qty:1});LT.saveCart(c);},
 remove(i){const c=LT.cart();c.splice(i,1);LT.saveCart(c);},
 setFmt(i,fmt){const c=LT.cart();c[i].fmt=fmt;LT.saveCart(c);},
 setQty(i,q){const c=LT.cart();c[i].qty=Math.max(1,Math.min(99,q|0));LT.saveCart(c);},
 clear(){LT.saveCart([]);},
 total(){return LT.cart().reduce((s,x)=>s+LT.PRICE*(x.qty||1),0);},
 count(){return LT.cart().length;},
 // accounts
 accounts(){try{return JSON.parse(localStorage.getItem('lt_accounts')||'{}');}catch(e){return{};}},
 user(){try{return JSON.parse(localStorage.getItem('lt_user')||'null');}catch(e){return null;}},
 signup(o){const a=LT.accounts();if(a[o.email])return {ok:false,msg:'An account with that email already exists — try signing in.'};
   a[o.email]=o;localStorage.setItem('lt_accounts',JSON.stringify(a));
   localStorage.setItem('lt_user',JSON.stringify({email:o.email,name:o.name,church:o.church,size:o.size}));return {ok:true};},
 signin(email,pw){const a=LT.accounts();const u=a[email];
   if(!u)return {ok:false,msg:'No account found for that email. You can create one in seconds.'};
   if(u.pw!==pw)return {ok:false,msg:'That password doesn\u2019t match. Try again.'};
   localStorage.setItem('lt_user',JSON.stringify({email:u.email,name:u.name,church:u.church,size:u.size}));return {ok:true};},
 signout(){localStorage.removeItem('lt_user');location.href='index.html';},
 orders(){try{return JSON.parse(localStorage.getItem('lt_orders')||'[]');}catch(e){return[];}},
 placeOrder(bill){const o={num:'LT-'+Date.now().toString(36).toUpperCase(),date:new Date().toLocaleDateString(),
   items:LT.cart(),total:LT.total(),bill,user:LT.user()&&LT.user().email};
   const os=LT.orders();os.unshift(o);localStorage.setItem('lt_orders',JSON.stringify(os));
   localStorage.setItem('lt_lastorder',JSON.stringify(o));LT.clear();return o;},
 lastOrder(){try{return JSON.parse(localStorage.getItem('lt_lastorder')||'null');}catch(e){return null;}},
 title(id){const r=(window.CAMPAIGNS||[]).find(x=>x[9]===id);return r?r[0]:id;},
 row(id){return (window.CAMPAIGNS||[]).find(x=>x[9]===id);},
 badge(){const b=document.getElementById('ltcount');if(b)b.textContent=LT.count();},
 injectNav(){
   const nr=document.querySelector('.nright, .nav-right');if(!nr)return;
   const cartBtn=document.createElement('a');cartBtn.className='btn btn-white';cartBtn.href='cart.html';
   cartBtn.style.cssText='padding:11px 14px;gap:6px;';
   cartBtn.innerHTML='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="21" r="1.6"/><circle cx="19" cy="21" r="1.6"/><path d="M2 3h3l2.6 12.5a2 2 0 0 0 2 1.5h8.9a2 2 0 0 0 2-1.6L22 7H6"/></svg><span id="ltcount">'+LT.count()+'</span>';
   nr.insertBefore(cartBtn,nr.firstChild);
   const u=LT.user();
   if(u){const links=[...nr.querySelectorAll('a')];
     links.forEach(a=>{const t=(a.textContent||'').trim();
       if(t==='Sign in'){a.href='account.html';a.textContent=u.name.split(' ')[0];}
       if(t.indexOf('Get access')===0){a.href='account.html';a.innerHTML='My account';}});}
 }
};
window.LT=LT;
document.addEventListener('DOMContentLoaded',function(){LT.injectNav();});
})();
