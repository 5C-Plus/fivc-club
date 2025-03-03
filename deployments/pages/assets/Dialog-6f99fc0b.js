import{_ as e}from"./ContentWrap.vue_vue_type_script_setup_true_lang-5554e0b6.js";import{_ as o}from"./Dialog.vue_vue_type_style_index_0_lang-466704f2.js";import{d as t,k as l,r as i,q as a,o as s,h as m,w as r,g as p,a as n,B as d,t as u,c,F as j,G as f,e as _,cM as v}from"./index-c922549f.js";import{E as g}from"./el-button-3322aa8d.js";import{F as b}from"./Form-e7ce6a0e.js";import{u as D}from"./useValidator-bed50dac.js";import"./el-card-a447f2d0.js";import"./el-tooltip-4ed993c7.js";import"./el-popper-777547bb.js";import"./isNil-1f22f7b0.js";import"./index-d069b56e.js";import"./constants-84857360.js";import"./focus-trap-8b9664b6.js";import"./el-dialog-4f02e0ff.js";import"./el-overlay-51fc3bc1.js";import"./scroll-2bae90a4.js";import"./vnode-9e1e4265.js";import"./use-dialog-10a356f2.js";import"./event-5568c9d8.js";import"./refs-99024eba.js";import"./index-075fce49.js";import"./use-form-item-04993e5b.js";import"./use-form-common-props-cca367ba.js";import"./el-form-item-969f14b2.js";import"./el-row-b1864fd0.js";import"./el-input-5992562e.js";/* empty css               */import"./el-checkbox-8ac95930.js";import"./isEqual-9f3d5ffd.js";import"./el-date-picker-62bfc5e6.js";import"./utils-627bb44a.js";import"./panel-time-pick-619bf4c7.js";import"./index-90b96cbe.js";import"./debounce-6961f983.js";import"./localeData-97fc05ae.js";import"./index-1f214b38.js";import"./el-input-number-e9628339.js";import"./el-select-2d83cd87.js";import"./index-c4f3a95b.js";import"./validator-ea5284a6.js";import"./el-switch-6b1b0237.js";import"./el-time-picker-b9f9e86a.js";import"./el-divider-9c627bce.js";import"./InputPassword-4808e8fc.js";import"./_plugin-vue_export-helper-1b428a4d.js";import"./style.css_vue_type_style_index_0_src_true_lang-f404ea13.js";import"./aria-ecee1d93.js";import"./tsxHelper-5aa3deb4.js";const y=t({__name:"Dialog",setup(t){const{required:y}=D(),{t:k}=l(),x=i(!1),h=i(!1),P=a([{field:"field1",label:k("formDemo.input"),component:"Input",formItemProps:{rules:[y()]}},{field:"field2",label:k("formDemo.select"),component:"Select",componentProps:{options:[{label:"option1",value:"1"},{label:"option2",value:"2"}]}},{field:"field3",label:k("formDemo.radio"),component:"Radio",componentProps:{options:[{label:"option-1",value:"1"},{label:"option-2",value:"2"}]}},{field:"field4",label:k("formDemo.checkbox"),component:"Checkbox",value:[],componentProps:{options:[{label:"option-1",value:"1"},{label:"option-2",value:"2"},{label:"option-3",value:"3"}]}},{field:"field5",component:"DatePicker",label:k("formDemo.datePicker"),componentProps:{type:"date"}},{field:"field6",component:"TimeSelect",label:k("formDemo.timeSelect")}]);(async()=>{const e=await v();e&&(P[1].componentProps.options=e.data)})();const C=i(),V=()=>{var e,o;null==(o=null==(e=n(C))?void 0:e.getElFormRef())||o.validate((e=>{}))};return(t,l)=>(s(),m(n(e),{title:n(k)("dialogDemo.dialog"),message:n(k)("dialogDemo.dialogDes")},{default:r((()=>[p(n(g),{type:"primary",onClick:l[0]||(l[0]=e=>x.value=!x.value)},{default:r((()=>[d(u(n(k)("dialogDemo.open")),1)])),_:1}),p(n(g),{type:"primary",onClick:l[1]||(l[1]=e=>h.value=!h.value)},{default:r((()=>[d(u(n(k)("dialogDemo.combineWithForm")),1)])),_:1}),p(n(o),{modelValue:x.value,"onUpdate:modelValue":l[3]||(l[3]=e=>x.value=e),title:n(k)("dialogDemo.dialog")},{footer:r((()=>[p(n(g),{onClick:l[2]||(l[2]=e=>x.value=!1)},{default:r((()=>[d(u(n(k)("dialogDemo.close")),1)])),_:1})])),default:r((()=>[(s(),c(j,null,f(1e4,(e=>_("div",{key:e},u(e),1))),64))])),_:1},8,["modelValue","title"]),p(n(o),{modelValue:h.value,"onUpdate:modelValue":l[5]||(l[5]=e=>h.value=e),title:n(k)("dialogDemo.dialog")},{footer:r((()=>[p(n(g),{type:"primary",onClick:V},{default:r((()=>[d(u(n(k)("dialogDemo.submit")),1)])),_:1}),p(n(g),{onClick:l[4]||(l[4]=e=>h.value=!1)},{default:r((()=>[d(u(n(k)("dialogDemo.close")),1)])),_:1})])),default:r((()=>[p(n(b),{ref_key:"formRef",ref:C,schema:P},null,8,["schema"])])),_:1},8,["modelValue","title"])])),_:1},8,["title","message"]))}});export{y as default};
