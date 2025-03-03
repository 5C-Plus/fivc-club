import{_ as e}from"./ContentWrap.vue_vue_type_script_setup_true_lang-5554e0b6.js";import{_ as t}from"./Search.vue_vue_type_script_setup_true_lang-1648bb08.js";import{d as a,u as o,k as i,q as s,A as l,r,o as m,h as p,w as n,g as d,a as c,e as u,B as j,t as g}from"./index-c922549f.js";import{E as _}from"./el-button-3322aa8d.js";/* empty css               */import{_ as b}from"./Table.vue_vue_type_script_lang-620172e0.js";import{g as f,d as x}from"./index-34858fc7.js";import{u as h}from"./useTable-648f0114.js";import{u as y}from"./useEmitt-089b34c8.js";import{u as v}from"./useCrudSchemas-645b7b50.js";import{E as D}from"./index-c4f3a95b.js";import"./el-card-a447f2d0.js";import"./el-tooltip-4ed993c7.js";import"./el-popper-777547bb.js";import"./isNil-1f22f7b0.js";import"./index-d069b56e.js";import"./constants-84857360.js";import"./focus-trap-8b9664b6.js";import"./Form-e7ce6a0e.js";import"./el-form-item-969f14b2.js";import"./use-form-common-props-cca367ba.js";import"./el-row-b1864fd0.js";import"./el-input-5992562e.js";import"./event-5568c9d8.js";import"./use-form-item-04993e5b.js";import"./el-checkbox-8ac95930.js";import"./isEqual-9f3d5ffd.js";import"./el-date-picker-62bfc5e6.js";import"./utils-627bb44a.js";import"./panel-time-pick-619bf4c7.js";import"./index-90b96cbe.js";import"./debounce-6961f983.js";import"./localeData-97fc05ae.js";import"./index-1f214b38.js";import"./el-input-number-e9628339.js";import"./el-select-2d83cd87.js";import"./index-075fce49.js";import"./scroll-2bae90a4.js";import"./validator-ea5284a6.js";import"./el-switch-6b1b0237.js";import"./el-time-picker-b9f9e86a.js";import"./el-divider-9c627bce.js";import"./InputPassword-4808e8fc.js";import"./_plugin-vue_export-helper-1b428a4d.js";import"./style.css_vue_type_style_index_0_src_true_lang-f404ea13.js";import"./aria-ecee1d93.js";import"./tsxHelper-5aa3deb4.js";import"./useForm-fd215ebe.js";import"./el-table-column-afd5a8b4.js";import"./el-pagination-952f169c.js";import"./el-message-box-e080817e.js";import"./el-overlay-51fc3bc1.js";import"./vnode-9e1e4265.js";import"./tree-b59d36bb.js";const w={class:"mb-10px"},k=a({name:"ExamplePage"}),S=a({...k,setup(a){const{push:k}=o(),{register:S,tableObject:C,methods:P}=h({getListApi:f,delListApi:x,response:{list:"list",total:"total"}}),{getList:R,setSearchParams:E}=P;R(),y({name:"getList",callback:e=>{"add"===e&&(C.currentPage=1),R()}});const{t:L}=i(),z=s([{field:"index",label:L("tableDemo.index"),type:"index"},{field:"title",label:L("tableDemo.title"),search:{show:!0}},{field:"author",label:L("tableDemo.author")},{field:"displayTime",label:L("tableDemo.displayTime")},{field:"importance",label:L("tableDemo.importance"),formatter:(e,t,a)=>l(D,{type:1===a?"success":2===a?"warning":"danger"},(()=>L(1===a?"tableDemo.important":2===a?"tableDemo.good":"tableDemo.commonly")))},{field:"pageviews",label:L("tableDemo.pageviews")},{field:"content",label:L("exampleDemo.content"),table:{show:!1}},{field:"action",width:"260px",label:L("tableDemo.action")}]),{allSchemas:A}=v(z),T=()=>{k("/example/example-add")},F=r(!1),U=async(e,t)=>{var a;C.currentRow=e;const{delList:o,getSelections:i}=P,s=await i();F.value=!0,await o(t?s.map((e=>e.id)):[null==(a=C.currentRow)?void 0:a.id],t).finally((()=>{F.value=!1}))},$=(e,t)=>{k(`/example/example-${t}?id=${e.id}`)};return(a,o)=>(m(),p(c(e),null,{default:n((()=>[d(c(t),{schema:c(A).searchSchema,onSearch:c(E),onReset:c(E)},null,8,["schema","onSearch","onReset"]),u("div",w,[d(c(_),{type:"primary",onClick:T},{default:n((()=>[j(g(c(L)("exampleDemo.add")),1)])),_:1}),d(c(_),{loading:F.value,type:"danger",onClick:o[0]||(o[0]=e=>U(null,!0))},{default:n((()=>[j(g(c(L)("exampleDemo.del")),1)])),_:1},8,["loading"])]),d(c(b),{pageSize:c(C).pageSize,"onUpdate:pageSize":o[1]||(o[1]=e=>c(C).pageSize=e),currentPage:c(C).currentPage,"onUpdate:currentPage":o[2]||(o[2]=e=>c(C).currentPage=e),columns:c(A).tableColumns,data:c(C).tableList,loading:c(C).loading,pagination:{total:c(C).total},onRegister:c(S)},{action:n((({row:e})=>[d(c(_),{type:"primary",onClick:t=>$(e,"edit")},{default:n((()=>[j(g(c(L)("exampleDemo.edit")),1)])),_:2},1032,["onClick"]),d(c(_),{type:"success",onClick:t=>$(e,"detail")},{default:n((()=>[j(g(c(L)("exampleDemo.detail")),1)])),_:2},1032,["onClick"]),d(c(_),{type:"danger",onClick:t=>U(e,!1)},{default:n((()=>[j(g(c(L)("exampleDemo.del")),1)])),_:2},1032,["onClick"])])),_:1},8,["pageSize","currentPage","columns","data","loading","pagination","onRegister"])])),_:1}))}});export{S as default};
