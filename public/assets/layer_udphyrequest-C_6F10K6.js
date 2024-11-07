import{r as l,b as o,j as t,a as c,g as u}from"./index-9mx06GO8.js";import{S as y}from"./SelectGroupTwo-Cq6A5zsc.js";import{C as h}from"./cardEnableLayer-DELu8wh0.js";const j=()=>{let[e,m]=l.useState({enabled:!1,u:{listen:":36718",exclude:"",net:"",cert:o()+"/layers/cfgs/my.crt",key:o()+"binary/layers/cfgs/my.key",obfs:"",max_conn_client:5e5}}),[x,d]=l.useState(0),[a,b]=l.useState([{NetName:"",Ip:""}]),s=()=>{b([...a]),m({...e})},n=()=>{c.get("/api/read/udp?"+u()).then(r=>{a=r.data.extra.networks,r.data.service.length>0?(e.u=r.data.service[0],e.enabled=!0,a.forEach((f,p,g)=>{f.NetName==e.u.net&&d(p)})):(e.enabled=!1,e.u={listen:":36718",exclude:"",net:"",cert:o()+"/layers/cfgs/my.crt",key:o()+"binary/layers/cfgs/my.key",obfs:"",max_conn_client:5e5},d(0)),s()}).catch(r=>{})};return l.useEffect(()=>{n()},[]),t.jsx(t.Fragment,{children:t.jsxs("div",{className:"w-full",children:[t.jsx(h,{enabled:e.enabled,onChange:r=>{e.enabled=r,s()}}),t.jsx("div",{className:"flex flex-row justify-center mt-5",children:t.jsxs("div",{className:"flex flex-col w-3/5 p-4 shadow-2 bg-white  md:w-3/5 w-4/5",children:[t.jsx("h4",{className:"mb-1 mt-2 font-bold font-sans  text-black dark:text-white",children:"Configure UDPHyRequest"}),t.jsx("p",{className:"text-xs text-gray-200 mb-2",children:"ports can be excluded from iptables separated by comma: mandatory 53,5300"}),t.jsx("input",{placeholder:"53,5300",value:e.u.exclude,onChange:r=>{e.u.exclude=r.target.value,s()},type:"text",className:" rounded-lg border-[1.5px] border-stroke bg-transparent py-3 px-5 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"}),t.jsx("p",{className:"text-xs text-gray-200 mb-2 mt-2 ",children:"Chose your network interface  to internet"}),t.jsx(y,{selOption:x,NetworkList:a,CallSelected:r=>{e.u.net=a[r].NetName,s(),d(r)}}),t.jsx("p",{className:"text-xs text-gray-200 mb-2 mt-2 ",children:"The obfuscated password"}),t.jsx("input",{placeholder:"Key OBFS",value:e.u.obfs,onChange:r=>{e.u.obfs=r.target.value,s()},type:"text",className:" rounded-lg border-[1.5px] border-stroke bg-transparent py-3 px-5 text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"}),t.jsx("div",{className:"w-full flex flex-row justify-center",children:t.jsx("button",{onClick:()=>{e.u.exclude!=""&&!e.enabled&&!confirm("are you sure you want to disable this layer?")||c.post("/api/layer/udp?"+u(),e).then(r=>{let i=e.enabled?"UDP  layer updated":"UDP Mix layer disabled and deleted parameters";alert(i),n()})},className:"w-3/4 mt-2 flex w-full cursor-pointer justify-center rounded bg-sky-800 p-3 font-medium text-gray hover:bg-opacity-90",children:"Save UDPHyRequest Layer"})})]})})]})})};export{j as default};