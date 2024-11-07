import{r as n,c as j,j as e,a as h,g as m}from"./index-9mx06GO8.js";const b=r=>{const[l,d]=n.useState(r.isChecked);let o=j();return e.jsx("div",{children:e.jsxs("label",{htmlFor:o,className:"flex cursor-pointer select-none items-center",children:[e.jsxs("div",{className:"relative",children:[e.jsx("input",{type:"checkbox",id:o,className:"sr-only",onChange:()=>{r.Onchange(!l),d(!l)}}),e.jsx("div",{className:`mr-4 flex h-5 w-5 items-center justify-center rounded border ${l&&"border-primary bg-gray dark:bg-transparent"}`,children:e.jsx("span",{className:`h-2.5 w-2.5 rounded-sm ${l&&"bg-primary"}`})})]}),r.Caption]})})};function v(){let r=new Date;return`${r.getFullYear()}-${r.getMonth()+1}-${r.getDate()}`}const i=r=>e.jsxs(e.Fragment,{children:[e.jsx("label",{className:"mb-3 block text-sm font-medium text-black dark:text-white",children:r.label}),e.jsx("input",{value:r.val,onChange:r.callbackChange,disabled:r.isDisabled,type:r.type,placeholder:r.placeholder,className:"rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"})]}),k=()=>{let[r,l]=n.useState(!1),[d,o]=n.useState(!1),[a,g]=n.useState({username:"",password:"",expdisable:!1,expire:v()}),[u,f]=n.useState([]),c=()=>{f([...u])},p=()=>{h.post("/api/read/user?"+m(),{}).then(s=>{u=s.data,c()})};n.useEffect(()=>{p()},[]);let x=s=>{g({...s})};return e.jsx(e.Fragment,{children:e.jsxs("div",{className:" with-overflow-vh",children:[e.jsxs("div",{className:"flex flex-col",children:[e.jsxs("div",{className:"flex p-4 shadow-2 bg-white mr-2 mt-2  ml-2 justify-between items-center",children:[e.jsx("h1",{children:"Create users"}),e.jsx("div",{onClick:()=>{o(!1),l(!r)},className:"bg-indigo-100 p-2 rounded-md cursor-pointer",children:e.jsx("svg",{xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24","stroke-width":"1.5",stroke:"currentColor",className:" transition size-6 "+(r?"rotate-180":"rotate-0"),children:e.jsx("path",{"stroke-linecap":"round","stroke-linejoin":"round",d:"m19.5 8.25-7.5 7.5-7.5-7.5"})})})]}),e.jsxs("div",{className:"ml-2 mr-2 shadow-2 bg-white transition-all flex flex-row gap-8 lg:gap-0 flex-wrap  justify-between items-center p-3 "+(r?"block":"hidden"),children:[e.jsx("div",{children:e.jsx(i,{val:a.username,callbackChange:s=>{a.username=s.target.value,x(a)},type:"text",label:"Username",placeholder:"your username",isDisabled:!1})}),e.jsx("div",{children:e.jsx(i,{val:a.password,callbackChange:s=>{a.password=s.target.value,x(a)},type:"text",label:"Password",placeholder:"your password",isDisabled:!1})}),e.jsx("div",{children:e.jsx(b,{isChecked:a.expdisable,Onchange:()=>{a.expdisable=!a.expdisable,x(a)},Caption:"Disable expire"})}),e.jsx("div",{children:e.jsx(i,{val:a.expire,callbackChange:s=>{a.expire=s.target.value,x(a)},isDisabled:a.expdisable,type:"date",label:"expiration",placeholder:""})}),e.jsx("div",{children:e.jsx("button",{onClick:()=>{h.post("/api/create/user?"+m(),a).then(s=>{alert("User created successfully"),a.username="",a.password="",x(a),p()}).catch(s=>{if(s.response.data){alert(s.response.data.detail);return}alert(s.message)})},className:"flex cursor-pointer justify-center rounded bg-sky-800 p-3 font-medium text-gray hover:bg-opacity-90",children:"Create user"})})]})]}),e.jsxs("div",{className:"flex flex-col",children:[e.jsxs("div",{className:"flex p-4 shadow-2 bg-white mr-2 mt-2  ml-2 justify-between items-center ",children:[e.jsx("h1",{children:"Manage registered users"}),e.jsx("div",{onClick:()=>{l(!1),o(!d)},className:"bg-indigo-100 p-2 rounded-md cursor-pointer",children:e.jsx("svg",{xmlns:"http://www.w3.org/2000/svg",fill:"none",viewBox:"0 0 24 24","stroke-width":"1.5",stroke:"currentColor",className:" transition size-6 "+(d?"rotate-180":"rotate-0"),children:e.jsx("path",{"stroke-linecap":"round","stroke-linejoin":"round",d:"m19.5 8.25-7.5 7.5-7.5-7.5"})})})]}),e.jsx("div",{className:"ml-2 mr-2 shadow-2 bg-white transition "+(d?"block":"hidden"),children:u.map(s=>e.jsx(e.Fragment,{children:e.jsxs("div",{className:"flex flex-row gap-8 lg:gap-0 flex-wrap  justify-between items-center p-3 ",children:[e.jsx("div",{children:e.jsx(i,{val:s.username,callbackChange:t=>{s.username=t.target.value,c()},type:"text",label:"Username",placeholder:"your username",isDisabled:!1})}),e.jsx("div",{children:e.jsx(i,{val:s.password,callbackChange:t=>{s.password=t.target.value,c()},type:"text",label:"Password",placeholder:"your password",isDisabled:!1})}),e.jsx("div",{children:e.jsx(b,{Caption:"Disable expire",isChecked:s.expdisable,Onchange:function(t){s.expdisable=t,c()}})}),e.jsx("div",{children:e.jsx(i,{val:s.expire,callbackChange:t=>{s.expire=t.target.value,c()},type:"date",label:"expiration",placeholder:"",isDisabled:!1})}),e.jsxs("div",{onClick:()=>{},className:"flex flex-row gap-3",children:[e.jsx("button",{onClick:()=>{h.post("/api/modify/user?"+m(),s).then(t=>{alert("User "+s.username+" Updated"),p()}).catch(t=>{alert("Error update "+s.username)})},className:"flex cursor-pointer justify-center rounded bg-green-600 p-3 font-medium text-gray hover:bg-opacity-90",children:"Update user"}),e.jsx("button",{onClick:()=>{confirm("Are your sure delete "+s.username)&&h.post("/api/delete/user?"+m(),{id:s.id}).then(t=>{alert("User "+s.username+" Deleted"),p()}).catch(t=>{alert("Error delete "+s.username)})},className:"flex cursor-pointer justify-center rounded bg-rose-800 p-3 font-medium text-gray hover:bg-opacity-90",children:"Delete user"})]})]})}))})]})]})})};export{k as default};
