import{d as e,r as a,v as l,z as t,D as s,o,h as u,w as d,c as i,G as r,F as n,a as m,x as p,k as c,e as f,t as b}from"./index-c922549f.js";import{E as g,a as v}from"./el-select-2d83cd87.js";import"./el-input-5992562e.js";/* empty css               */import"./el-popper-777547bb.js";import{g as h,l as y}from"./index-cbebeb66.js";const V={style:{float:"left","margin-right":"5px"}},j=e({__name:"ParticipantSelect",props:{modelValue:{default:""},size:{default:"default"},clearable:{type:Boolean,default:!1},disabled:{type:Boolean,default:!1}},emits:["update:modelValue"],setup(e,{emit:j}){const _=e,{t:x}=c(),z=a([]),w=a(!1),k=l({get:()=>_.modelValue,set(e){j("update:modelValue",e)}}),B=async(e="")=>{let a=[],l=m(k);const t=l;if(w.value=!0,l)try{const e=await h(l);a.push(e)}catch(s){l=""}try{const t=(await y({name_contains:e})).results.filter((e=>e.uuid!==l));a=a.concat(t),_.clearable||l||!a.length||(l=a[0].uuid)}finally{(!t&&l||t&&!l)&&(k.value=l),z.value=a,w.value=!1}};return t((()=>{B()})),s((()=>{B()})),(e,a)=>(o(),u(m(g),{modelValue:m(k),"onUpdate:modelValue":a[0]||(a[0]=e=>p(k)?k.value=e:null),loading:w.value,placeholder:m(x)("configs.program"),size:_.size,disabled:_.disabled,clearable:_.clearable,remote:!0,"remote-method":B,filterable:""},{default:d((()=>[(o(!0),i(n,null,r(z.value,(e=>(o(),u(m(v),{key:e.uuid,label:e.name,value:e.uuid},{default:d((()=>[f("span",V,b(e.name),1)])),_:2},1032,["label","value"])))),128))])),_:1},8,["modelValue","loading","placeholder","size","disabled","clearable"]))}});export{j as _};
