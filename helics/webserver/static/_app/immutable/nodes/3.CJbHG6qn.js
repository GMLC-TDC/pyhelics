import{A as e,B as t,D as n,G as r,I as i,P as a,R as o,T as s,V as c,W as l,X as u,Y as d,_ as f,_t as ee,b as te,bt as p,ct as ne,ft as m,g as h,h as g,k as _,lt as v,mt as y,n as b,nt as re,ot as x,p as ie,st as ae,u as oe,ut as S,v as C,vt as se,x as ce}from"../chunks/CBKHL9ry.js";import"../chunks/DokDqs8w.js";import{t as le}from"../chunks/BqXrKsxe.js";import{t as ue}from"../chunks/BIXHt038.js";import{o as de}from"../chunks/CWp9l9sX.js";var w=o(`<button type="button" class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Clear Barrier</button>`),T=o(`<div class="flex justify-center"><div class="block p-6 border border-gray-200 bg-white w-full"><h5 class="text-gray-900 text-xl leading-tight font-medium mb-2"> </h5> <p class="text-gray-700 text-base mb-4"> <br/> <br/> <br/> <br/> <!></p> <div class="flex space-x-2"><button type="button" class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out">Delete</button> <button type="button" class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out" data-twe-toggle="modal">Set Barrier</button> <!></div></div></div> <div class="modal fade fixed z-[1050] top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto" tabindex="-1" aria-labelledby="broker-set-barrier-model-title" aria-modal="true" role="dialog"><div data-twe-modal-dialog-ref="" class="modal-dialog modal-dialog-centered relative w-auto pointer-events-none"><div class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"><div class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-gray-200 rounded-t-md"><h5 class="text-xl font-medium leading-normal text-gray-800" id="broker-set-barrier-model-label">Modal title</h5> <button type="button" class="btn-close box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline" data-twe-modal-dismiss="" aria-label="Close"></button></div> <div data-twe-modal-body-ref="" class="modal-body relative p-4"><label for="broker-barrier-time-input" class="form-label inline-block mb-2 text-gray-700">Broker Barrier Time:</label> <input type="number" class="
        form-control
        block
        w-full
        px-3
        py-1.5
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding
        border border-solid border-gray-300
        rounded
        transition
        ease-in-out
        m-0
        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
      " id="broker-barrier-time-input" placeholder="0"/></div> <div class="modal-footer flex flex-shrink-0 flex-wrap items-center justify-end p-4 border-t border-gray-200 rounded-b-md"><button type="button" class="inline-block px-6 py-2.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out" data-twe-modal-dismiss="">Close</button> <button type="button" data-twe-modal-dismiss="">Set Barrier</button></div></div></div></div>`,1);function fe(e,o){se(o,!1);let s=b(o,`broker`,24,()=>({})),d=b(o,`callback`,8,async()=>{}),f=b(o,`broker_barrier_time`,12,null),_=b(o,`barrierDialogId`,8),y=S(!1),C=`/api/v1`;async function le(){s()&&await fetch(`${C}/brokers/${s().name}`,{method:`DELETE`,mode:`cors`}),await d()()}async function de(e){let t=await fetch(`${C}/brokers/${s().name}/time-barrier`,{method:`PUT`,mode:`cors`,headers:{Accept:`application/json`,"Content-Type":`application/json`},body:JSON.stringify({time:e})});await d()(),t.status==200?m(y,!0):console.log(t)}async function fe(){let e=await fetch(`${C}/brokers/${s().name}/time-barrier`,{method:`DELETE`,mode:`cors`,headers:{Accept:`application/json`,"Content-Type":`application/json`}});await d()(),e.status==200?m(y,!1):console.log(e)}oe();var E=T(),D=ae(E),O=x(D),k=x(O),pe=ne(k),A=v(k,2),j=x(A),M=v(j,2),N=v(M,2),P=v(N,2),me=v(P,3),he=e=>{var n=t();re(()=>a(n,`Barrier Time: ${f()??``}`)),i(e,n)};n(me,e=>{r(y)&&f()!=null&&f()!=null&&e(he)}),p(A);var F=v(A,2),I=x(F),L=v(I,2);ce(L,e=>ue?.(e));var R=v(L,2),z=e=>{var t=w();c(`click`,t,fe),i(e,t)};n(R,e=>{r(y)&&e(z)}),p(F),p(O),p(D);var B=v(D,2),V=x(B),H=x(V),U=v(x(H),2),W=v(x(U),2);g(W),p(U);var G=v(U,2),K=v(x(G),2);p(G),p(H),p(V),p(B),re(()=>{a(pe,`Name: ${l(s()),u(()=>s().name)??``}`),a(j,`Address: ${l(s()),u(()=>s().address)??``} `),a(M,` Is Connected: ${l(s()),u(()=>s().is_connected)??``} `),a(N,` Is Open: ${l(s()),u(()=>s().is_open_to_new_federates)??``} `),a(P,` Is Root: ${l(s()),u(()=>s().is_root)??``} `),h(L,`data-twe-target`,`#`+_()),h(B,`id`,_()),te(K,1,`inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md focus:outline-none focus:ring-0 transition duration-150 ease-in-out ml-1
          ${f()==null?`pointer-events-none opacity-60`:`hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 active:bg-blue-800 active:shadow-lg focus:shadow-lg`}`),K.disabled=f()==null}),c(`click`,I,le),ie(W,f),c(`click`,K,()=>de(f())),i(e,E),ee()}var E=o(`<button type="button" data-mdb-ripple="true" data-mdb-ripple-color="light" class="inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out" data-twe-toggle="modal" data-twe-target="#create-broker-model">Create New Broker</button>`),D=o(`<div class="py-2">FastAPI server is up and running.</div>`),O=o(`<li class="px-6 py-4 w-full"><!></li>`),k=o(`<div class="grow grid grid-areas-layout justify-items-stretch my-auto py-6"><div class="flex justify-center w-full"><ul class="bg-white rounded-lg border border-gray-200 w-full text-gray-900 py-4"><h4 class="px-6 py-2 font-medium leading-tight text-2xl mt-0 mb-2 text-blue-600 border-b border-gray-200">Brokers</h4> <!></ul></div></div>`),pe=o(`<div class="flex w-7/8 flex-col mt-6 mx-8"><div class="overflow-x-auto sm:-mx-6 lg:-mx-8"><div class="py-2 inline-block w-full sm:px-6 lg:px-8"><div class="flex justify-between"><div class="flex space-x-4 items-center"><span class="text-gray-700"> </span> <!></div> <!></div> <div class="flex flex-col h-full"><div class="grow grid grid-areas-layout justify-items-stretch my-auto"><!></div> <!></div></div></div></div> <div class="modal fade fixed z-[1050] top-0 left-0 hidden w-full h-full outline-none overflow-x-hidden overflow-y-auto" id="create-broker-model" tabindex="-1" aria-labelledby="create-broker-model-title" aria-modal="true" role="dialog"><div data-twe-modal-dialog-ref="" class="modal-dialog modal-dialog-centered relative w-auto pointer-events-none"><div class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"><div class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-gray-200 rounded-t-md"><h5 class="text-xl font-medium leading-normal text-gray-800">Create Broker</h5> <button type="button" class="btn-close box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline" data-twe-modal-dismiss="" aria-label="Close"></button></div> <div data-twe-modal-body-ref="" class="modal-body relative p-4"><label for="broker-name-input" class="form-label inline-block mb-2 text-gray-700">Broker Name:</label> <input type="text" class="
        form-control
        block
        w-full
        px-3
        py-1.5
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding
        border border-solid border-gray-300
        rounded
        transition
        ease-in-out
        m-0
        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
      " id="broker-name-input" placeholder="broker-name"/></div> <div data-twe-modal-body-ref="" class="modal-body relative p-4"><label for="broker-port-input" class="form-label inline-block mb-2 text-gray-700">Broker Port:</label> <input type="text" class="
        form-control
        block
        w-full
        px-3
        py-1.5
        text-base
        font-normal
        text-gray-700
        bg-white bg-clip-padding
        border border-solid border-gray-300
        rounded
        transition
        ease-in-out
        m-0
        focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none
      " id="broker-port-input" placeholder="23404"/></div> <div data-twe-modal-body-ref="" class="modal-body relative p-4"><label for="broker-core-type-input" class="form-label inline-block mb-2 text-gray-700">Broker Core Type:</label> <select id="broker-core-type-input" class="form-select appearance-none
            block
            w-full
            px-3
            py-1.5
            text-base
            font-normal
            text-gray-700
            bg-white bg-clip-padding bg-no-repeat
            border border-solid border-gray-300
            rounded
            transition
            ease-in-out
            m-0
            focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" aria-label="Core Type"><option>ZMQ</option><option>TCP</option><option>UDP</option></select></div> <div data-twe-modal-body-ref="" class="modal-body relative p-4"><label for="broker-log-level-input" class="form-label inline-block mb-2 text-gray-700">Broker Log Level:</label> <select id="broker-core-type-input" class="form-select appearance-none
            block
            w-full
            px-3
            py-1.5
            text-base
            font-normal
            text-gray-700
            bg-white bg-clip-padding bg-no-repeat
            border border-solid border-gray-300
            rounded
            transition
            ease-in-out
            m-0
            focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" aria-label="Log Level"><option>debug</option><option>trace</option><option>info</option><option>error</option><option>warning</option><option>none</option><option>data</option><option>connections</option><option>interfaces</option><option>profiling</option><option>summary</option><option>timing</option></select></div> <div class="modal-footer flex flex-shrink-0 flex-wrap items-center justify-end p-4 border-t border-gray-200 rounded-b-md"><button type="button" class="inline-block px-6 py-2.5 bg-purple-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-purple-700 hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out" data-twe-modal-dismiss="">Close</button> <button type="button" data-twe-modal-dismiss="">Create</button></div></div></div></div>`,1);function A(t,o){se(o,!1);let l=S(!1),u=S([]),h=S(!0),b=S(!1),w=null,T=S(`Broker1`),A=S(23404),j=S(`zmq`),M=S(`info`),N=`/api/v1`;async function P(){await me(),await he()}e(async()=>{await P(),await d(),m(h,!1),clearInterval(w),w=setInterval(async()=>{await P(),await d()},5e3)}),_(()=>{clearInterval(w)});async function me(){try{let e=await fetch(`${N}/health`),t=await e.json();m(l,e.ok&&t.status===`ok`),m(b,r(l)),r(l)&&console.log(`Healthy server`)}catch{console.log(`Unable to reach server`),m(l,!1)}}async function he(){if(r(l)){let e=await(await fetch(`${N}/brokers`)).json();e&&m(u,e.brokers)}}async function F(e,t,n,i){if(r(l)){(t===``||t===null)&&(t=23404);let r={name:e,port:t,log_level:i,core_type:n};console.log(JSON.stringify({broker:e,port:t,log_level:i,core_type:n})),m(h,!0);let a=await fetch(`${N}/brokers`,{method:`POST`,mode:`cors`,headers:{Accept:`application/json`,"Content-Type":`application/json`},body:JSON.stringify(r)});console.log(a),await P(),m(h,!1)}}oe();var I=pe(),L=ae(I),R=x(L),z=x(R),B=x(z),V=x(B),H=x(V),U=ne(H),W=v(H,2);le(W,{get icon(){return de},get spin(){return r(h)}}),p(V);var G=v(V,2),K=e=>{var t=E();ce(t,e=>ue?.(e)),i(e,t)};n(G,e=>{r(l)&&e(K)}),p(B);var ge=v(B,2),q=x(ge),_e=x(q),ve=e=>{var t=D();i(e,t)};n(_e,e=>{r(l)&&e(ve)}),p(q);var ye=v(q,2),be=e=>{var t=k(),n=x(t),a=x(n),o=v(x(a),2);s(o,3,()=>r(u),e=>e.name,(e,t,n)=>{var a=O(),o=x(a);{let e=y(()=>`broker-barrier-${r(n)}`);fe(o,{get broker(){return r(t)},get barrierDialogId(){return r(e)},callback:P})}p(a),i(e,a)}),p(a),p(n),p(t),i(e,t)};n(ye,e=>{r(l)&&e(be)}),p(ge),p(z),p(R),p(L);var xe=v(L,2),Se=x(xe),Ce=x(Se),J=v(x(Ce),2),we=v(x(J),2);g(we),p(J);var Y=v(J,2),Te=v(x(Y),2);g(Te),p(Y);var X=v(Y,2),Z=v(x(X),2),Ee=x(Z);Ee.value=Ee.__value=`zmq`;var De=v(Ee);De.value=De.__value=`tcp`;var Oe=v(De);Oe.value=Oe.__value=`udp`,p(Z),C(Z),p(X);var ke=v(X,2),Q=v(x(ke),2),Ae=x(Q);Ae.value=Ae.__value=`debug`;var je=v(Ae);je.value=je.__value=`trace`;var Me=v(je);Me.value=Me.__value=`info`;var Ne=v(Me);Ne.value=Ne.__value=`error`;var Pe=v(Ne);Pe.value=Pe.__value=`warning`;var Fe=v(Pe);Fe.value=Fe.__value=`none`;var Ie=v(Fe);Ie.value=Ie.__value=`data`;var Le=v(Ie);Le.value=Le.__value=`connections`;var Re=v(Le);Re.value=Re.__value=`interfaces`;var ze=v(Re);ze.value=ze.__value=`profiling`;var Be=v(ze);Be.value=Be.__value=`summary`;var Ve=v(Be);Ve.value=Ve.__value=`timing`,p(Q),C(Q),p(ke);var He=v(ke,2),$=v(x(He),2);p(He),p(Ce),p(Se),p(xe),re(()=>{a(U,`FastAPI service: ${r(b)?`online`:`offline`}`),te($,1,`inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md focus:outline-none focus:ring-0 transition duration-150 ease-in-out ml-1
          ${r(T)===``?`pointer-events-none opacity-60`:`hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 active:bg-blue-800 active:shadow-lg focus:shadow-lg`}`),$.disabled=r(T)==``}),ie(we,()=>r(T),e=>m(T,e)),ie(Te,()=>r(A),e=>m(A,e)),f(Z,()=>r(j),e=>m(j,e)),f(Q,()=>r(M),e=>m(M,e)),c(`click`,$,async()=>await F(r(T),r(A),r(j),r(M))),i(t,I),ee()}export{A as component};