import{j as e,r as l,a as t,g as i}from"./index-9mx06GO8.js";const c=s=>e.jsx("div",{className:"rounded-sm border border-stroke bg-white px-5 pt-6 pb-2.5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1",children:e.jsxs("div",{className:"flex flex-col",children:[e.jsx("div",{className:"grid grid-cols-1 rounded-sm bg-gray-2 dark:bg-meta-4 sm:grid-cols-1",children:e.jsx("div",{className:"p-2.5 xl:p-5",children:e.jsx("h5",{className:"text-sm font-medium uppercase xsm:text-base",children:"Service information"})})}),e.jsx("div",{className:"grid grid-cols-1 sm:grid-cols-1 ",children:s.Logs.map((r,a)=>e.jsx(e.Fragment,{children:e.jsx("div",{className:"flex items-center gap-3 p-1 xl:p-1",children:e.jsx("p",{className:"hidden text-black dark:text-white sm:block",children:r})})}))})]})}),x=()=>{let[s,r]=l.useState([]),a=()=>{t.get("/api/logs?"+i()).then(d=>{r(d.data)})};return l.useEffect(()=>{a()},[]),e.jsx(e.Fragment,{children:e.jsx("div",{className:"w-full",children:e.jsx("div",{className:"flex flex-row justify-center mt-5",children:e.jsx("div",{className:"flex flex-col w-3/5 p-4 shadow-2 bg-white  md:w-3/5 w-4/5 with-overflow-vh",children:e.jsx(c,{Logs:s})})})})})};export{x as default};