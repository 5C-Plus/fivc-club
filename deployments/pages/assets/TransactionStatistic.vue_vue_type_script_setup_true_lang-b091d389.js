import{d as t,r as a,C as e,z as s,o as r,h as n,w as o,g as i,a as l}from"./index-c922549f.js";import{E as u}from"./el-card-a447f2d0.js";import{E as c,a as d}from"./el-row-b1864fd0.js";import{E as m}from"./el-skeleton-item-9edfbad7.js";import{_ as p}from"./Echart.vue_vue_type_script_setup_true_lang-2b70c0fe.js";import{o as f}from"./index-186e8914.js";const h=t({__name:"EchartTime",props:{title:{default:""},timeType:{default:"date"},isStacked:{type:Boolean,default:!1},isZoomable:{type:Boolean,default:!1},data:null,dataTypes:null,dataColors:null,tooltipFormatter:null,refreshVersion:{default:0},width:null,height:null},setup(t){const o=t,i={title:{text:""},tooltip:{trigger:"axis",formatter:t=>t},grid:{left:50,right:50,containLabel:!1},xAxis:{type:"time",boundaryGap:!1,axisTick:{show:!1},axisLabel:{rotate:40,formatter:t=>t}},yAxis:{type:"value",axisTick:{show:!1},axisLabel:{formatter:t=>t}},legend:{type:"scroll",top:30,data:[]},series:[]},l=a({...i}),u=()=>{if(!o.data)return;const t=o.dataTypes,a=o.dataColors,e=Array.from(o.data.keys()),s=Array.from(o.data.entries()).map((e=>{const s=e[0],r={name:s,type:"line",data:e[1],animationDuration:1e3,symbol:"none"};if(t){const a=t.get(s);a&&(r.type=a)}if(a){const t=a.get(s);t&&(r.itemStyle={color:t})}return o.isStacked&&(r.stack="Total",r.areaStyle={}),r})),r={...i};r.title.text=o.title,r.legend.data=e,r.series=s,"date"===o.timeType?r.xAxis.axisLabel.formatter=t=>new Date(t).toLocaleDateString():r.xAxis.axisLabel.formatter=t=>new Date(t).toLocaleString(),l.value=r};return e((()=>o.refreshVersion),(async()=>{await u()})),s((()=>{u()})),(t,a)=>(r(),n(p,{options:l.value,width:o.width,height:o.height},null,8,["options","width","height"]))}}),y=t({__name:"TransactionStatistic",props:{refreshVersion:{default:0},clubUuid:{default:""},accountUuid:{default:""},extraParams:null},setup(t){const p=t,y=new Map,_=a(y),x=new Map([["Balance","line"],["Income","bar"],["Expenditure","bar"]]),w=a(0),g=a(!1),v=async()=>{try{g.value=!0,_.value=y;const t=[],a=[],e=[],s={club:p.clubUuid,account:p.accountUuid,transact_time_zone:Intl.DateTimeFormat().resolvedOptions().timeZone};p.extraParams&&Object.assign(s,p.extraParams);{let a=0;const e=await f(s);for(const s of e.results)a+=s.transact_amount,t.push([new Date(s.transact_date),a])}{const t=await f({transact_amount_gte:0,...s});for(const e of t.results)a.push([new Date(e.transact_date),e.transact_amount])}{const t=await f({transact_amount_lt:0,...s});for(const a of t.results)e.push([new Date(a.transact_date),a.transact_amount])}const r=new Map([["Balance",t]]);a.length&&r.set("Income",a),e.length&&r.set("Expenditure",e),_.value=r,w.value+=1}catch(t){_.value=y}finally{g.value=!1}};return e((()=>p.refreshVersion),(async()=>{await v()})),e((()=>p.extraParams),(async()=>{await v()})),e((()=>p.accountUuid),(async()=>{await v()})),e((()=>p.clubUuid),(async()=>{await v()})),s((()=>{v()})),(t,a)=>(r(),n(l(d),null,{default:o((()=>[i(l(c),{span:24},{default:o((()=>[i(l(m),{loading:g.value},{default:o((()=>[i(l(u),{shadow:"hover",style:{margin:"10px"}},{default:o((()=>[i(l(h),{"refresh-version":w.value,data:_.value,"data-types":l(x),"time-type":"date",height:300},null,8,["refresh-version","data","data-types"])])),_:1})])),_:1},8,["loading"])])),_:1})])),_:1}))}});export{y as _};
