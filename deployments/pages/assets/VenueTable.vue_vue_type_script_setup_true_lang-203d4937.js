import{d as e,r as a,v as t,a as l,C as n,D as o,z as s,H as r,I as i,o as c,h as u,w as m,g as d,J as p,B as f,t as g,K as y,e as _,x as b,k as w,E as h}from"./index-c922549f.js";import{a as x,E as k}from"./el-button-3322aa8d.js";/* empty css                        */import{E as v}from"./el-card-a447f2d0.js";import{a as j,E as C}from"./el-row-b1864fd0.js";import{E}from"./el-input-5992562e.js";import{E as z}from"./el-message-box-e080817e.js";import"./el-overlay-51fc3bc1.js";import{E as U}from"./el-pagination-952f169c.js";/* empty css               */import"./el-select-2d83cd87.js";import{E as V}from"./el-popper-777547bb.js";import{E as B,a as S}from"./el-table-column-afd5a8b4.js";import"./el-checkbox-8ac95930.js";import"./el-tooltip-4ed993c7.js";import{f as T,h as D}from"./index-51cc2b47.js";const K={style:{"white-space":"pre-wrap","word-break":"break-word"}},I=e({__name:"VenueTable",props:{refreshVersion:{default:0},clubUuid:{default:""}},emits:["create","edit"],setup(e,{emit:I}){const J=e,{t:L}=w(),M=a([]),W=a(0),A=a(!1),F=a({offset:0,limit:30,address_contains:""}),H=t({get(){const e=l(F);return e.offset/e.limit+1},set(e){const a=l(F);a.offset=(e-1)*a.limit}}),P=t({get:()=>l(F).limit,set(e){l(F).limit=e}}),X=async()=>{try{A.value=!0;const e={club:J.clubUuid,...l(F)},a=await T(e);W.value=a.count||0,M.value=a.results}catch(e){W.value=0,M.value=[]}finally{A.value=!1}};return n((()=>J.refreshVersion),(async()=>{await X()})),n((()=>J.clubUuid),(async()=>{await X()})),o((()=>{X()})),s((()=>{X()})),(e,a)=>{const t=r("Icon"),n=i("loading");return c(),u(l(j),null,{default:m((()=>[d(l(C),{span:24},{default:m((()=>[d(l(v),{"body-style":"padding: 0"},{header:m((()=>[d(l(j),null,{default:m((()=>[d(l(E),{modelValue:F.value.address_contains,"onUpdate:modelValue":a[0]||(a[0]=e=>F.value.address_contains=e),placeholder:l(L)("common.name"),style:{width:"200px","margin-right":"5px"},clearable:"",onKeydown:a[1]||(a[1]=p((e=>X()),["enter"]))},null,8,["modelValue","placeholder"]),d(l(x),null,{default:m((()=>[d(l(k),{type:"primary",onClick:a[2]||(a[2]=e=>{I("create")})},{default:m((()=>[f(g(l(L)("exampleDemo.add")),1)])),_:1}),d(l(k),{onClick:a[3]||(a[3]=e=>X())},{default:m((()=>[d(l(V),{content:l(L)("router.search"),placement:"top"},{default:m((()=>[d(t,{icon:"ep:search"})])),_:1},8,["content"])])),_:1})])),_:1})])),_:1})])),default:m((()=>[y((c(),u(l(B),{data:M.value},{default:m((()=>[d(l(S),{label:l(L)("meetings.venueAddress"),align:"center"},{default:m((({row:e})=>[_("span",K,g(e.address),1)])),_:1},8,["label"]),d(l(S),{label:l(L)("common.createdBy"),align:"center","min-width":30},{default:m((({row:e})=>[d(l(j),null,{default:m((()=>[d(l(C),null,{default:m((()=>[f(g(e.created_by),1)])),_:2},1024)])),_:2},1024),d(l(j),null,{default:m((()=>[d(l(C),{style:{"font-size":"x-small"}},{default:m((()=>[f(g(new Date(e.created_time).toLocaleString()),1)])),_:2},1024)])),_:2},1024)])),_:1},8,["label"]),d(l(S),{label:l(L)("meetings.venueExternal"),align:"center","min-width":30},{default:m((({row:e})=>[e.external?(c(),u(t,{key:1,icon:"material-symbols:link",style:{cursor:"pointer"},onClick:a=>(e=>{e.external&&window.open(e.external,"_blank")})(e)},null,8,["onClick"])):(c(),u(t,{key:0,icon:"material-symbols:link"}))])),_:1},8,["label"]),d(l(S),{label:l(L)("common.action"),align:"center"},{default:m((({row:e})=>[d(l(x),null,{default:m((()=>[d(l(k),{onClick:a=>(e=>{I("edit",l(e))})(e)},{default:m((()=>[d(t,{icon:"ep:edit"})])),_:2},1032,["onClick"]),d(l(k),{type:"danger",onClick:a=>(async e=>{try{await z.confirm(L("common.delMessage"),L("common.delWarning"),{confirmButtonText:L("common.ok"),cancelButtonText:L("common.cancel"),type:"warning"})}catch(a){return}try{await D(e.uuid),h({type:"success",message:L("common.delSuccess")})}catch(a){h({type:"error",message:L("common.delFailed")})}await X()})(e)},{default:m((()=>[d(t,{icon:"ep:delete"})])),_:2},1032,["onClick"])])),_:2},1024)])),_:1},8,["label"])])),_:1},8,["data"])),[[n,A.value]]),d(l(U),{"current-page":l(H),"onUpdate:currentPage":a[4]||(a[4]=e=>b(H)?H.value=e:null),"page-size":l(P),"onUpdate:pageSize":a[5]||(a[5]=e=>b(P)?P.value=e:null),total:W.value,layout:"prev, pager, next, jumper, sizes, total",style:{margin:"10px"},onSizeChange:a[6]||(a[6]=e=>X()),onCurrentChange:a[7]||(a[7]=e=>X())},null,8,["current-page","page-size","total"])])),_:1})])),_:1})])),_:1})}}});export{I as _};
