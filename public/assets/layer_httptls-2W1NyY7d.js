import{r as o,b as l,j as e,a as d,g as c}from"./index-9mx06GO8.js";import{C as m}from"./cardEnableLayer-DELu8wh0.js";const b=()=>{let[t,h]=o.useState({enabled:!1,ht:[{Http:{Response:""},Tls:{Cert:l()+"/cfg/cert.pem",Key:l()+"/cfg/key.pem"},Listen:""}]}),s=()=>{h({...t})},x=()=>{d.get("/api/read/httptls?"+c()).then(r=>{r.data.length>0?(t.enabled=!0,t.ht=r.data):(t.enabled=!1,t.ht=[{Http:{Response:""},Tls:{Cert:l()+"/cfg/cert.pem",Key:l()+"/cfg/key.pem"},Listen:""}]),s()}).catch(r=>{})};o.useEffect(()=>{x()},[]);let p=()=>{t.ht.push({Http:{Response:""},Tls:{Cert:l()+"/cfg/cert.pem",Key:l()+"/cfg/key.pem"},Listen:""}),s()},f=r=>{let a=t.ht.filter((i,n)=>n!=r);t.ht=a,s()};return e.jsx(e.Fragment,{children:e.jsxs("div",{className:"w-full",children:[e.jsx(m,{enabled:t.enabled,onChange:r=>{t.enabled=r,s()}}),e.jsx("div",{className:"flex flex-row justify-center mt-5",children:e.jsxs("div",{className:"flex flex-col w-3/5 p-4 shadow-2 bg-white  md:w-3/5 w-4/5 with-overflow-vh",children:[e.jsx("h4",{className:"mb-1 mt-2 font-bold font-sans  text-black dark:text-white",children:"Listen layer(s) SSL/TLS"}),e.jsx("p",{className:"text-xs text-gray-200 mb-2",children:"The configurations are similar to HTTP, however this type of HTTP TLS layer allows you to create a connection where an SSL/TLS connection is first established and once an HTTP packet is sent within said connection, the parameters, as you will understand, are the mix between the HTTP layer and also TLS,"}),t.ht.map((r,a)=>{let i=a==t.ht.length-1;return e.jsx(e.Fragment,{children:e.jsxs("div",{className:"flex flex-col",children:[e.jsxs("div",{className:"w-full flex flex-row justify-between items-center",children:[e.jsx("p",{className:"text-xs text-gray-200 mb-2 ",children:"The SSL/TLS Layer server address : 0.0.0.0:443"}),a>0&&e.jsx("a",{onClick:()=>{f(a)},href:"#",className:" px-2 py-2 text-center text-xs text-primary ",children:"Delete this layer"})]}),e.jsx("input",{value:r.Listen,onChange:n=>{r.Listen=n.target.value,s()},type:"text",className:" rounded-lg border-[1.5px] border-stroke bg-transparent py-3 px-5 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"}),e.jsx("p",{className:"text-xs text-gray-200 mb-2 mt-2 ",children:"The HTTP Response in the HTTP connection"}),e.jsx("input",{value:r.Http.Response,onChange:n=>{r.Response=n.target.value,s()},type:"text",className:" rounded-lg border-[1.5px] border-stroke bg-transparent py-3 px-5 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"}),i&&e.jsx("div",{className:"w-full flex flex-row justify-end",children:e.jsx("a",{onClick:()=>p(),href:"#",className:" px-2 py-2 text-center text-xs text-primary ",children:"Add new layer"})})]})})}),e.jsx("div",{className:"w-full flex flex-row justify-center",children:e.jsx("button",{onClick:()=>{(t.ht[0].Listen!=""||t.ht.length>0)&&!t.enabled&&!confirm("are you sure you want to disable this layer?")||d.post("/api/layer/httptls?"+c(),t).then(r=>{let a=t.enabled?"HTTP/TLS Mix layer updated":"HTTP/TLS Mix layer disabled and deleted parameters";alert(a)})},className:"w-3/4 mt-2 flex w-full cursor-pointer justify-center rounded bg-sky-800 p-3 font-medium text-gray hover:bg-opacity-90",children:"Save HTTP/TLS Layer"})})]})})]})})};export{b as default};