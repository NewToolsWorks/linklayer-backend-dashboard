import{j as e,r as l,a as o,g as c}from"./index-9mx06GO8.js";import{S as u}from"./SelectGroupTwo-Cq6A5zsc.js";import{C as w}from"./cardEnableLayer-DELu8wh0.js";const p=t=>e.jsx(e.Fragment,{children:e.jsxs("div",{className:"flex mb-8 w-full border-l-6 border-[#34D399] bg-[#34D399] bg-opacity-[15%] px-2 py-2 shadow-md dark:bg-[#1B1B24] dark:bg-opacity-30 md:p-2",children:[e.jsx("div",{className:"mr-5 flex h-9 w-full max-w-[36px] items-center justify-center rounded-lg bg-[#34D399]",children:e.jsx("svg",{width:"16",height:"12",viewBox:"0 0 16 12",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:e.jsx("path",{d:"M15.2984 0.826822L15.2868 0.811827L15.2741 0.797751C14.9173 0.401867 14.3238 0.400754 13.9657 0.794406L5.91888 9.45376L2.05667 5.2868C1.69856 4.89287 1.10487 4.89389 0.747996 5.28987C0.417335 5.65675 0.417335 6.22337 0.747996 6.59026L0.747959 6.59029L0.752701 6.59541L4.86742 11.0348C5.14445 11.3405 5.52858 11.5 5.89581 11.5C6.29242 11.5 6.65178 11.3355 6.92401 11.035L15.2162 2.11161C15.5833 1.74452 15.576 1.18615 15.2984 0.826822Z",fill:"white",stroke:"white"})})}),e.jsxs("div",{className:"w-full",children:[e.jsx("h5",{className:"text-sm font-semibold text-black dark:text-[#34D399] ",children:t.Title}),e.jsx("p",{className:"text-sm leading-relaxed text-body break-words",children:t.Content})]})]})}),k=()=>{let[t,x]=l.useState({enabled:!1,d:{Domain:"",Net:""}}),[r,m]=l.useState({public:"",networks:[{Ip:"",NetName:""}]}),[f,n]=l.useState(0),s=()=>{x({...t}),m({...r})},d=()=>{o.get("/api/read/dnstt?"+c()).then(a=>{r=a.data.extra,a.data.service.length>0?(t.d=a.data.service[0],t.enabled=!0,a.data.extra.networks.forEach((h,b,N)=>{h.NetName==t.d.Net&&n(b)})):(t.enabled=!1,t.d={Domain:"",Net:""},n(0)),s()}).catch(a=>{})};return l.useEffect(()=>{d()},[]),e.jsx(e.Fragment,{children:e.jsxs("div",{className:"w-full",children:[e.jsx(w,{enabled:t.enabled,onChange:a=>{t.enabled=a,s()}}),e.jsx("div",{className:"flex flex-row justify-center mt-5",children:e.jsxs("div",{className:"flex flex-col w-3/5 p-4 shadow-2 bg-white  md:w-3/5 w-4/5",children:[e.jsx("h4",{className:"mb-1 mt-2 font-bold font-sans  text-black dark:text-white",children:"Configure DNSTT"}),e.jsx("p",{className:"text-xs text-gray-200 mb-2",children:"Parameters needed to create a DNSTT connection"}),e.jsx(p,{Title:"Your public Key 👇 👇 👇",Content:r.public}),e.jsxs("div",{className:"flex flex-col",children:[e.jsx("div",{className:"w-full flex flex-row justify-between items-center",children:e.jsx("p",{className:"text-xs text-gray-200 mb-2 ",children:"Domain required example: ns.linklayer.com"})}),e.jsx("input",{value:t.d.Domain,onChange:a=>{t.d.Domain=a.target.value,s()},type:"text",className:" rounded-lg border-[1.5px] border-stroke bg-transparent py-3 px-5 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"}),e.jsx("p",{className:"text-xs text-gray-200 mb-2 mt-2 ",children:"Choose the network interface remember:  if you use more than 1, check which one has access to the Internet."}),e.jsx(u,{selOption:f,NetworkList:r.networks,CallSelected:a=>{t.d.Net=r.networks[a].NetName,n(a),s()}})]}),e.jsx("div",{className:"w-full flex flex-row justify-center",children:e.jsx("button",{onClick:()=>{t.d.Domain!=""&&!t.enabled&&!confirm("are you sure you want to disable this layer?")||o.post("/api/layer/dnstt?"+c(),t).then(a=>{let i=t.enabled?"DNSTT  layer updated":"DNSTT Mix layer disabled and deleted parameters";alert(i),d()})},className:"w-3/4 mt-2 flex w-full cursor-pointer justify-center rounded bg-sky-800 p-3 font-medium text-gray hover:bg-opacity-90",children:"Save HTTP/TLS Layer"})})]})})]})})};export{k as default};
