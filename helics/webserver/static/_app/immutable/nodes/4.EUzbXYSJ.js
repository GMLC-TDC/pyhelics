import{$ as e,A as t,D as n,E as r,G as i,I as a,L as o,P as s,R as c,T as l,V as u,W as d,X as f,_t as p,a as m,b as h,bt as g,ct as _,et as v,ft as y,ht as b,i as x,lt as S,mt as C,n as w,nt as T,o as E,ot as D,s as O,st as k,u as ee,ut as A,vt as j,yt as M}from"../chunks/CBKHL9ry.js";import"../chunks/DokDqs8w.js";import{t as N}from"../chunks/BqXrKsxe.js";import{n as P,t as F}from"../chunks/CWp9l9sX.js";import{i as I,n as L,t as R}from"../chunks/BoDQu3Ph.js";import{a as z,t as B}from"../chunks/pzfobp7H.js";var V=c(`<button><!></button>`),te=c(`<th scope="col" class="text-sm font-medium text-white px-6 py-4 text-left"><div class="flex"><span> </span> &nbsp; <!> <!></div></th>`),ne=c(`<td class="px-6 py-4 whitespace text-sm font-medium text-gray-900"> </td>`),H=c(`<tr class="border-b hover:bg-gray-100"></tr>`),re=c(`<span class="px-2 py-3"> </span> <div class="dropdown relative"><button class="
          dropdown-toggle
          px-2
          py-3
          bg-blue-600
          text-white
          font-medium
          text-xs
          leading-tight
          uppercase
          rounded
          shadow-md
          hover:bg-blue-700 hover:shadow-lg
          focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0
          active:bg-blue-800 active:shadow-lg active:text-white
          transition
          duration-150
          ease-in-out
          flex
          items-center
          whitespace-nowrap
        " type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false"> <span class="px-1"></span> <!></button> <ul class="
          dropdown-menu
          min-w-max
          absolute
          bg-white
          text-base
          z-50
          float-left
          py-3
          list-none
          text-left
          rounded-lg
          shadow-lg
          mt-1
          hidden
          m-0
          bg-clip-padding
          border-none
        "><li><button class="
              dropdown-item
              text-sm
              py-2.5
              px-6
              font-normal
              block
              w-full
              whitespace-nowrap
              bg-transparent
              text-gray-700
              hover:bg-gray-100
            ">10</button></li> <li><button class="
              dropdown-item
              text-sm
              py-2.5
              px-6
              font-normal
              block
              w-full
              whitespace-nowrap
              bg-transparent
              text-gray-700
              hover:bg-gray-100
            ">25</button></li></ul></div> <span class="px-2 py-3">rows per page.</span>`,1),U=c(`<li><button> </button></li>`),ie=c(`<ul class="flex  list-style-none"><li><button aria-label="Previous"><span aria-hidden="true">&laquo;</span></button></li> <!> <li><button aria-label="Next"><span aria-hidden="true">&raquo;</span></button></li></ul>`),W=c(`<div class="flex w-full flex-col my-2"><div class="flex w-full justify-between"><button type="button" class="inline-block px-6 py-1.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg"><!></button></div></div> <table class="table-auto w-full"><thead class="border-b bg-gray-800"><tr></tr></thead><tbody></tbody></table> <div class="flex w-full justify-between mb-12"><div class="flex justify-center"><!></div> <nav aria-label="Page navigation example"><!></nav></div>`,1);function G(t,c){j(c,!1);let m=A(),b=A(),x=A(),E=A(),O=A(),I=w(c,`data`,28,()=>[]),L=w(c,`columns`,28,()=>[]),R=w(c,`showAll`,12,!1),z=w(c,`N`,12,10);function B(e){let t=e?I().length+1:z();var n=[{number:1,active:!0}];for(let[e,r]of I().entries())e%t===0&&e>0&&(n=[...n,{number:e/t+1,active:!1}]);return n}function G(e){for(var t of i(b))t.active=t.number===e;y(b,i(b))}function K(e){for(let t of L())t.title==e.title?(t.sortActive&&(t.sort=t.sort==`ascending`?`descending`:`ascending`),t.sortActive=!0):t.sortActive=!1;L(L()),I(I())}function ae(e){for(let t of L())if(t.sortActive){t.sort==`ascending`?e.sort((e,n)=>{let r=e[t.sortName],i=n[t.sortName];return r=r==`-`?0:r,i=i==`-`?0:i,r<i?-1:+(r>i)}):t.sort==`descending`&&e.sort((e,n)=>{let r=e[t.sortName],i=n[t.sortName];return r=r==`-`?0:r,i=i==`-`?0:i,r>i?-1:+(r<i)});break}return e}e(()=>(d(R()),d(I()),d(z())),()=>{y(m,R()?I().length+1:z())}),e(()=>d(R()),()=>{y(b,B(R()))}),e(()=>i(b),()=>{y(x,i(b).length===1||i(b)[0].active)}),e(()=>i(b),()=>{y(E,i(b).length===1||i(b).at(-1).active)}),e(()=>i(b),()=>{y(O,i(b).findIndex(e=>e.active))}),e(()=>d(I()),()=>{ae(I())}),v(),ee();var oe=W(),q=k(oe),se=D(q),J=D(se),ce=D(J),le=e=>{N(e,{get icon(){return P}})},ue=e=>{N(e,{get icon(){return F}})};n(ce,e=>{R()?e(le):e(ue,-1)}),g(J),g(se),g(q);var Y=S(q,2),X=D(Y),Z=D(X);l(Z,5,L,r,(e,t)=>{var r=te(),o=D(r),c=D(o),l=_(c,!0),d=S(c,2),p=e=>{var n=V(),r=D(n);{let e=C(()=>(i(t),f(()=>i(t).sortActive?i(t).sortColor:`#aaa`)));N(r,{get style(){return`color: ${i(e)??``}`},get icon(){return F}})}g(n),u(`click`,n,()=>K(i(t))),a(e,n)};n(d,e=>{i(t),f(()=>i(t).sort==`ascending`)&&e(p)});var m=S(d,2),h=e=>{var n=V(),r=D(n);{let e=C(()=>(i(t),f(()=>i(t).sortActive?i(t).sortColor:`#aaa`)));N(r,{get style(){return`color: ${i(e)??``}`},get icon(){return P}})}g(n),u(`click`,n,()=>K(i(t))),a(e,n)};n(m,e=>{i(t),f(()=>i(t).sort==`descending`)&&e(h)}),g(o),g(r),T(()=>s(l,(i(t),f(()=>i(t).title)))),a(e,r)}),g(Z),g(X);var de=S(X);l(de,7,I,e=>e,(e,t,c)=>{var u=o(),d=k(u),p=e=>{var n=H();l(n,5,L,r,(e,n)=>{var r=ne(),o=_(r,!0);T(()=>s(o,(i(t),i(n),f(()=>i(t)[i(n).field])))),a(e,r)}),g(n),a(e,n)};n(d,e=>{i(c)>=i(O)*i(m)&&i(c)<(i(O)+1)*i(m)&&e(p)}),a(e,u)}),g(de),g(Y);var Q=S(Y,2),$=D(Q),fe=D($),pe=e=>{var t=re(),n=k(t),r=_(n),o=S(n,2),c=D(o),l=D(c),p=S(l,3);N(p,{get icon(){return F}}),g(c);var m=S(c,2),h=D(m),v=_(h),y=S(h,2),b=_(y);g(m),g(o),M(2),T(e=>{s(r,`Showing ${z()*i(O)+1} to ${e??``} of
        ${d(I()),f(()=>I().length)??``} rows with`),s(l,`${z()??``} `)},[()=>(d(z()),i(O),d(I()),f(()=>Math.min(z()*(i(O)+1),I().length)))]),u(`click`,v,()=>z(10)),u(`click`,b,()=>z(25)),a(e,t)};n(fe,e=>{R()||e(pe)}),g($);var me=S($,2),he=D(me),ge=e=>{var t=ie(),n=D(t),r=_(n),o=S(n,2);l(o,1,()=>i(b),e=>e,(e,t)=>{var n=U(),r=D(n),o=_(r,!0);g(n),T(()=>{h(n,1,`page-item ${i(t),f(()=>i(t).active?`active`:``)??``}`),h(r,1,`page-link relative block py-1.5 px-3 border-0 outline-none rounded
                ${i(t),f(()=>i(t).active?`bg-blue-600 text-white hover:text-white hover:bg-blue-600 shadow-md focus:shadow-md`:`bg-transparent text-gray-800 hover:text-gray-800 hover:bg-gray-200 focus:shadow-none`)??``}
                  `),s(o,(i(t),f(()=>i(t).number)))}),u(`click`,r,e=>G(i(t).number)),a(e,n)});var c=S(o,2),d=_(c);g(t),T(()=>{h(n,1,`page-item ${i(x)?`disabled`:``}`),h(r,1,`page-link relative block py-1.5 px-3 rounded border-0 bg-transparent outline-none text-gray-800 focus:shadow-none
            ${i(x)?`pointer-events-none`:`hover:text-gray-800 hover:bg-gray-200`}`),h(c,1,`page-item  ${i(E)?`disabled`:``}`),h(d,1,`page-link relative block py-1.5 px-3 rounded border-0 bg-transparent outline-none text-gray-800 focus:shadow-none
            ${i(E)?`pointer-events-none`:`hover:text-gray-800 hover:bg-gray-200`}`)}),u(`click`,r,e=>G(1)),u(`click`,d,e=>G(i(b).length)),a(e,t)};n(he,e=>{R()||e(ge)}),g(me),g(Q),u(`click`,J,e=>R(!R())),a(t,oe),p()}var K=c(`<div class="flex flex-col h-[55vh] py-4"><div class="grow grid grid-areas-layout justify-items-stretch my-auto"><!></div></div>`);function ae(e,n){j(n,!1);let r=()=>m(L,`$data`,o),[o,s]=x();function c(e,t){let n=[],r=[],i={};n.push({name:`__broker__`,group:0});for(let e of t.cores)for(let t of e.federates){t.publications===void 0&&(t.publications=[]);for(let e of t.publications){n.push({name:`${e.federate}-${e.handle}`,federate:t.attributes.name,group:1}),e.targets===void 0&&(e.targets=[]),i[`${e.federate}-${e.handle}`]=e.key;for(let t of e.targets)r.push({source:`${e.federate}-${e.handle}`,target:`${t.federate}-${t.handle}`,label:i[`${e.federate}-${e.handle}`],ignore:!1})}}for(let e of t.cores)for(let t of e.federates){t.inputs===void 0&&(t.inputs=[]);for(let e of t.inputs){n.push({name:`${e.federate}-${e.handle}`,federate:t.attributes.name,group:2}),e.sources===void 0&&(e.sources=[]);for(let t of e.sources)r.push({source:`${t.federate}-${t.handle}`,target:`${e.federate}-${e.handle}`,label:i[`${t.federate}-${t.handle}`],ignore:!1})}}return n=Array.from(new Set(n.map(JSON.stringify))).map(JSON.parse),r=Array.from(new Set(r.map(JSON.stringify))).map(JSON.parse),{nodes:n,links:r}}let l=A();t(()=>{y(l,c(r().graphs.federate,r().graphs.data))}),ee();var u=K(),d=D(u),f=D(d);z(f,{get data(){return i(l)},children:(e,t)=>{B(e,{})},$$slots:{default:!0}}),g(d),g(u),a(e,u),p(),s()}var oe=c(`<p>Drag 'n' drop a observer generated "helics-cli.sqlite" file here, or click to select a
            "helics-cli.sqlite" file</p>`),q=c(`<div class="my-4"> </div>`),se=c(`<h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">Topology</h3> <!>`,1),J=c(`<h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">Cores</h3> <!>`,1),ce=c(`<h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">Federates</h3> <!>`,1),le=c(`<h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">Publications</h3> <!>`,1),ue=c(`<h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">Inputs</h3> <!>`,1),Y=c(`<h3 class="font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600">data</h3> <!>`,1),X=c(`<div class="flex w-7/8 flex-col mt-6 mx-8"><div class="overflow-x-auto sm:-mx-6 lg:-mx-8"><div class="py-2 inline-block w-full sm:px-6 lg:px-8"><div class="flex space-x-4"><!> <button type="button" class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Clear</button></div> <!> <!> <!> <!> <!> <!> <!></div></div></div>`);function Z(e,t){j(t,!1);let r=()=>m(L,`$data`,o),[o,c]=x(),l=`/api/v1/observer`;async function d(e,t){let n=await fetch(`${l}/${e}`);return n.ok?await n.json():t}function h(e){for(let t of r().cores)if(t.id==e)return t.name}function v(e){for(let t of r().federates)if(t.id==e)return t.name}async function y(){E(L,f(r).systeminfo=await d(`systeminfo`,{}),f(r)),E(L,f(r).cores=await d(`cores`,[]),f(r)),E(L,f(r).federates=await d(`federates`,[]),f(r)),r().federates.map(e=>e.core_name=h(e.parent)),E(L,f(r).federates=r().federates,f(r)),E(L,f(r).graphs=await d(`graphs`,{}),f(r)),E(L,f(r).publications=await d(`publications`,[]),f(r)),r().publications.map(e=>{e.source_name=v(e.source),e.target_name=v(e.target)}),E(L,f(r).publications=r().publications,f(r)),E(L,f(r).inputs=await d(`inputs`,[]),f(r)),r().inputs.map(e=>{e.source_name=v(e.source),e.target_name=v(e.target)}),E(L,f(r).inputs=r().inputs,f(r));function e(e){return e==`id`?`ID`:e==`simulation_time`?`Simulation Time`:e}E(L,f(r).table=await d(`data`,[]),f(r));let t=[];for(let n of Object.keys(r().table[0]||{}))n!=`updated_at`&&t.push({field:n,sortName:n,title:e(n),show:!0,sort:`ascending`,sortColor:`#fff`,sortActive:!0,text_center:!1});E(L,f(r).table_columns=t,f(r))}let C={accepted:[],rejected:[]};async function w(e){let{acceptedFiles:t,fileRejections:n}=e.detail;C.accepted=[...C.accepted,...t],C.rejected=[...C.rejected,...n];var r=new FormData;r.append(`file`,C.accepted.at(-1)),await fetch(`${l}/database`,{method:`POST`,body:r}),await y()}async function A(e){let t=r().profile;O(L,R),E(L,f(r).profile=t,f(r))}ee();var M=X(),N=D(M),P=D(N),F=D(P),z=D(F);I(z,{multiple:!1,$$events:{drop:w},children:(e,t)=>{var n=oe();a(e,n)},$$slots:{default:!0}});var B=S(z,2);g(F);var V=S(F,2),te=e=>{var t=q(),n=_(t);T(()=>s(n,`HELICS Version: ${r().systeminfo.version.string??``}`)),a(e,t)},ne=b(()=>Object.keys(r().systeminfo).length!=0);n(V,e=>{i(ne)&&e(te)});var H=S(V,2),re=e=>{var t=se();ae(S(k(t),2),{}),a(e,t)};n(H,e=>{r().table.length!=0&&e(re)});var U=S(H,2),ie=e=>{var t=J();G(S(k(t),2),{get data(){return r().cores},get columns(){return r().cores_columns}}),a(e,t)};n(U,e=>{r().cores.length!=0&&e(ie)});var W=S(U,2),K=e=>{var t=ce();G(S(k(t),2),{get data(){return r().federates},get columns(){return r().federates_columns}}),a(e,t)};n(W,e=>{r().federates.length!=0&&e(K)});var Z=S(W,2),de=e=>{var t=le();G(S(k(t),2),{get data(){return r().publications},get columns(){return r().publications_columns}}),a(e,t)};n(Z,e=>{r().publications.length!=0&&e(de)});var Q=S(Z,2),$=e=>{var t=ue();G(S(k(t),2),{get data(){return r().inputs},get columns(){return r().inputs_columns}}),a(e,t)};n(Q,e=>{r().inputs.length!=0&&e($)});var fe=S(Q,2),pe=e=>{var t=Y();G(S(k(t),2),{get data(){return r().table},get columns(){return r().table_columns}}),a(e,t)};n(fe,e=>{r().table.length!=0&&e(pe)}),g(P),g(N),g(M),u(`click`,B,A),a(e,M),p(),c()}export{Z as component};