import{d as e,r as a,v as t,a as l,C as o,z as n,H as s,I as r,o as i,h as m,w as c,g as p,J as u,B as d,t as f,K as g,x as y,k as _,E as v}from"./index-c922549f.js";import{a as j,E as b}from"./el-button-3322aa8d.js";/* empty css                        */import{E as h}from"./el-card-a447f2d0.js";import{a as x,E as w}from"./el-row-b1864fd0.js";import{E as C}from"./el-input-5992562e.js";import{E as k}from"./el-message-box-e080817e.js";import"./el-overlay-51fc3bc1.js";import{E}from"./el-pagination-952f169c.js";/* empty css               */import"./el-select-2d83cd87.js";import"./el-popper-777547bb.js";import{E as z,a as T}from"./el-table-column-afd5a8b4.js";import"./el-checkbox-8ac95930.js";import"./el-tooltip-4ed993c7.js";import{f as U,h as V}from"./index-cbebeb66.js";const B=e({__name:"ParticipantTitleTable",props:{refreshVersion:{default:0},participantUuid:{default:""}},emits:["create","edit"],setup(e,{emit:B}){const K=e,{t:S}=_(),I=a([]),M=a(0),P=a(!1),W=a({offset:0,limit:100,name_contains:""}),D=t({get(){const e=l(W);return e.offset/e.limit+1},set(e){const a=l(W);a.offset=(e-1)*a.limit}}),F=t({get:()=>l(W).limit,set(e){l(W).limit=e}}),H=async()=>{try{P.value=!0;const e={participant:K.participantUuid,...l(W)},a=await U(e);M.value=a.count||0,I.value=a.results}catch(e){M.value=0,I.value=[]}finally{P.value=!1}};return o((()=>K.refreshVersion),(async()=>{await H()})),n((()=>{H()})),(e,a)=>{const t=s("Icon"),o=r("loading");return i(),m(l(x),null,{default:c((()=>[p(l(w),{span:24},{default:c((()=>[p(l(h),{"body-style":"padding: 0"},{header:c((()=>[p(l(x),null,{default:c((()=>[p(l(C),{modelValue:W.value.name_contains,"onUpdate:modelValue":a[0]||(a[0]=e=>W.value.name_contains=e),placeholder:l(S)("common.name"),style:{width:"200px","margin-right":"5px"},clearable:"",onKeydown:a[1]||(a[1]=u((e=>H()),["enter"]))},null,8,["modelValue","placeholder"]),p(l(j),null,{default:c((()=>[p(l(b),{type:"primary",onClick:a[2]||(a[2]=e=>{B("create")})},{default:c((()=>[d(f(l(S)("exampleDemo.add")),1)])),_:1})])),_:1})])),_:1})])),default:c((()=>[g((i(),m(l(z),{data:I.value},{default:c((()=>[p(l(T),{label:l(S)("common.name"),align:"center",prop:"program_name"},null,8,["label"]),p(l(T),{label:l(S)("common.alias"),align:"center",prop:"program_alias","min-width":50},null,8,["label"]),p(l(T),{label:l(S)("common.level"),align:"center",prop:"level"},null,8,["label"]),p(l(T),{label:l(S)("common.action"),align:"center"},{default:c((({row:e})=>[p(l(j),null,{default:c((()=>[p(l(b),{onClick:a=>(e=>{B("edit",l(e))})(e)},{default:c((()=>[p(t,{icon:"ep:edit"})])),_:2},1032,["onClick"]),p(l(b),{type:"danger",onClick:a=>(async e=>{try{await k.confirm(S("common.delMessage"),S("common.delWarning"),{confirmButtonText:S("common.ok"),cancelButtonText:S("common.cancel"),type:"warning"})}catch(a){return}try{await V(e.uuid),v({type:"success",message:S("common.delSuccess")})}catch(a){v({type:"error",message:S("common.delFailed")})}await H()})(e)},{default:c((()=>[p(t,{icon:"ep:delete"})])),_:2},1032,["onClick"])])),_:2},1024)])),_:1},8,["label"])])),_:1},8,["data"])),[[o,P.value]]),p(l(E),{"current-page":l(D),"onUpdate:currentPage":a[3]||(a[3]=e=>y(D)?D.value=e:null),"page-size":l(F),"onUpdate:pageSize":a[4]||(a[4]=e=>y(F)?F.value=e:null),total:M.value,layout:"prev, pager, next, jumper, sizes, total",style:{margin:"10px"},onSizeChange:a[5]||(a[5]=e=>H()),onCurrentChange:a[6]||(a[6]=e=>H())},null,8,["current-page","page-size","total"])])),_:1})])),_:1})])),_:1})}}});export{B as _};
