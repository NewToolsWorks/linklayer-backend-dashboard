import{r as i,j as e,a as o,g as x}from"./index-BdWtd8kq.js";import{C as p}from"./cardEnableLayer-D2lrZUh0.js";const b=()=>{let[r,c]=i.useState({enabled:!1,h:[{Listen:"",Response:""}]}),s=()=>{c({...r})},n=()=>{o.get("/api/read/http?"+x()).then(t=>{t.data.length>0?(r.enabled=!0,r.h=t.data):(r.enabled=!1,r.h=[{Listen:"",Response:""}]),s()}).catch(t=>{})};i.useEffect(()=>{n()},[]);let h=()=>{r.h.push({Listen:"",Response:""}),s()},f=t=>{let a=r.h.filter((d,l)=>l!=t);r.h=a,s()};return e.jsx(e.Fragment,{children:e.jsxs("div",{className:"w-full",children:[e.jsx(p,{enabled:r.enabled,onChange:t=>{r.enabled=t,s()}}),e.jsx("div",{className:"flex flex-row justify-center mt-5",children:e.jsxs("div",{className:"flex flex-col w-3/5 p-4 shadow-2 bg-white with-overflow-vh  md:w-3/5 w-4/5",children:[e.jsx("h4",{className:"mb-1 mt-2 font-bold font-sans  text-black dark:text-white",children:"Listen layer(s) HTTP"}),r.h.map((t,a)=>{let d=a==r.h.length-1;return e.jsx(e.Fragment,{children:e.jsxs("div",{className:"flex flex-col",children:[e.jsxs("div",{className:"w-full flex flex-row justify-between items-center",children:[e.jsx("p",{className:"text-xs text-gray-200 mb-2 ",children:"The address where the example server will listen : 0.0.0.0:80"}),a>0&&e.jsx("a",{onClick:()=>{f(a)},href:"#",className:" px-2 py-2 text-center text-xs text-primary ",children:"Delete this layer"})]}),e.jsx("input",{value:t.Listen,onChange:l=>{t.Listen=l.target.value,s()},type:"text",className:" rounded-lg border-[1.5px] border-stroke bg-transparent py-3 px-5 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"}),e.jsx("p",{className:"text-xs text-gray-200 mb-2 mt-2 ",children:"Response HTTP example: HTTP/1.1 200 OK\\r\\n\\r\\n"}),e.jsx("input",{placeholder:"HTTP/1.1 200 OK\\r\\n\\r\\n",value:t.Response,onChange:l=>{t.Response=l.target.value,s()},type:"text",className:" rounded-lg border-[1.5px] border-stroke bg-transparent py-3 px-5 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"}),d&&e.jsx("div",{className:"w-full flex flex-row justify-end",children:e.jsx("a",{onClick:()=>{h()},href:"#",className:" px-2 py-2 text-center text-xs text-primary ",children:"Add new layer"})})]})})}),e.jsx("div",{className:"w-full flex flex-row justify-center",children:e.jsx("button",{onClick:()=>{(r.h[0].Listen!=""||r.h.length>0)&&!r.enabled&&!confirm("are you sure you want to disable this layer?")||o.post("/api/layer/http?"+x(),r).then(t=>{let a=r.enabled?"HTTP layer updated":"HTTP layer disabled and deleted parameters";alert(a),n()})},className:"w-3/4 mt-2 flex w-full cursor-pointer justify-center rounded bg-sky-800 p-3 font-medium text-gray hover:bg-opacity-90",children:"Save HTTP Layer"})})]})})]})})};export{b as default};
