import{F as e}from"./Form-e7ce6a0e.js";import{u as r}from"./useForm-fd215ebe.js";import{u as t}from"./useValidator-bed50dac.js";import{d as s,q as o,C as a,o as m,h as i,a as u}from"./index-c922549f.js";const n=s({__name:"Write",props:{currentRow:{type:Object,default:()=>null},formSchema:{type:Array,default:()=>[]}},setup(s,{expose:n}){const p=s,{required:l}=t(),c=o({title:[l()],author:[l()],importance:[l()],pageviews:[l()],displayTime:[l()],content:[l()]}),{register:f,methods:d,elFormRef:g}=r({schema:p.formSchema});return a((()=>p.currentRow),(e=>{if(!e)return;const{setValues:r}=d;r(e)}),{deep:!0,immediate:!0}),n({elFormRef:g,getFormData:d.getFormData}),(r,t)=>(m(),i(u(e),{rules:c,onRegister:u(f)},null,8,["rules","onRegister"]))}});export{n as _};
