import{k as e,q as a,v as t,C as n,r as s,a as o,b6 as i,E as l,ad as r}from"./index-c922549f.js";import{E as c}from"./el-message-box-e080817e.js";import"./el-button-3322aa8d.js";import"./el-input-5992562e.js";import"./el-overlay-51fc3bc1.js";const{t:u}=e(),g=e=>{const g=a({pageSize:10,currentPage:1,total:10,tableList:[],params:{...(null==e?void 0:e.defaultParams)||{}},loading:!0,currentRow:null}),p=t((()=>({...g.params,pageSize:g.pageSize,pageIndex:g.currentPage})));n((()=>g.currentPage),(()=>{w.getList()})),n((()=>g.pageSize),(()=>{1===g.currentPage||(g.currentPage=1),w.getList()}));const d=s(),m=s(),v=async()=>{await r();const e=o(d);return e},P=async a=>{if(await((null==e?void 0:e.delListApi)&&(null==e?void 0:e.delListApi(a)))){l.success(u("common.delSuccess"));const e=(g.total%g.pageSize===a.length||1===g.pageSize)&&g.currentPage>1?g.currentPage-1:g.currentPage;g.currentPage=e,w.getList()}},w={getList:async()=>{var a;g.loading=!0;const t=await(null==e?void 0:e.getListApi(o(p)).finally((()=>{g.loading=!1})));t&&(g.tableList=i(t.data||{},null==e?void 0:e.response.list),g.total=i(t.data||{},null==(a=null==e?void 0:e.response)?void 0:a.total)||0)},setProps:async(e={})=>{const a=await v();null==a||a.setProps(e)},setColumn:async e=>{const a=await v();null==a||a.setColumn(e)},getSelections:async()=>{const e=await v();return(null==e?void 0:e.selections)||[]},setSearchParams:e=>{g.currentPage=1,g.params=Object.assign(g.params,{pageSize:g.pageSize,pageIndex:g.currentPage,...e}),w.getList()},delList:async(e,a,t=!0)=>{const n=await v();if(a){if(!(null==n?void 0:n.selections.length))return void l.warning(u("common.delNoData"))}else if(!g.currentRow)return void l.warning(u("common.delNoData"));t?c.confirm(u("common.delMessage"),u("common.delWarning"),{confirmButtonText:u("common.delOk"),cancelButtonText:u("common.delCancel"),type:"warning"}).then((async()=>{await P(e)})):await P(e)}};return(null==e?void 0:e.props)&&w.setProps(e.props),{register:(e,a)=>{d.value=e,m.value=o(a)},elTableRef:m,tableObject:g,methods:w}};export{g as u};
