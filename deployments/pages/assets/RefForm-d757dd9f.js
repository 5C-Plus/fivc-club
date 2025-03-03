import{F as e}from"./Form-e7ce6a0e.js";import{_ as o}from"./ContentWrap.vue_vue_type_script_setup_true_lang-5554e0b6.js";import{d as l,k as t,q as i,r as a,o as m,c as r,g as s,w as n,a as p,B as d,t as f,F as u,cM as c}from"./index-c922549f.js";import{E as j}from"./el-button-3322aa8d.js";import{u as v}from"./useValidator-bed50dac.js";import"./el-form-item-969f14b2.js";import"./constants-84857360.js";import"./use-form-common-props-cca367ba.js";import"./index-d069b56e.js";import"./el-row-b1864fd0.js";import"./el-tooltip-4ed993c7.js";import"./el-popper-777547bb.js";import"./isNil-1f22f7b0.js";import"./focus-trap-8b9664b6.js";import"./el-input-5992562e.js";import"./event-5568c9d8.js";import"./use-form-item-04993e5b.js";/* empty css               */import"./el-checkbox-8ac95930.js";import"./isEqual-9f3d5ffd.js";import"./el-date-picker-62bfc5e6.js";import"./utils-627bb44a.js";import"./panel-time-pick-619bf4c7.js";import"./index-90b96cbe.js";import"./debounce-6961f983.js";import"./localeData-97fc05ae.js";import"./index-1f214b38.js";import"./el-input-number-e9628339.js";import"./el-select-2d83cd87.js";import"./index-c4f3a95b.js";import"./index-075fce49.js";import"./scroll-2bae90a4.js";import"./validator-ea5284a6.js";import"./el-switch-6b1b0237.js";import"./el-time-picker-b9f9e86a.js";import"./el-divider-9c627bce.js";import"./InputPassword-4808e8fc.js";import"./_plugin-vue_export-helper-1b428a4d.js";import"./style.css_vue_type_style_index_0_src_true_lang-f404ea13.js";import"./aria-ecee1d93.js";import"./tsxHelper-5aa3deb4.js";import"./el-card-a447f2d0.js";const b=l({__name:"RefForm",setup(l){const{required:b}=v(),{t:_}=t(),D=i([{field:"field1",label:_("formDemo.input"),component:"Input",formItemProps:{rules:[b()]}},{field:"field2",label:_("formDemo.select"),component:"Select",componentProps:{options:[{label:"option1",value:"1"},{label:"option2",value:"2"}]}},{field:"field3",label:_("formDemo.radio"),component:"Radio",componentProps:{options:[{label:"option-1",value:"1"},{label:"option-2",value:"2"}]}},{field:"field4",label:_("formDemo.checkbox"),component:"Checkbox",value:[],componentProps:{options:[{label:"option-1",value:"1"},{label:"option-2",value:"2"},{label:"option-3",value:"3"}]}},{field:"field5",component:"DatePicker",label:_("formDemo.datePicker"),componentProps:{type:"date"}},{field:"field6",component:"TimeSelect",label:_("formDemo.timeSelect")}]),k=a(),h=e=>{var o;null==(o=p(k))||o.setProps({labelWidth:e})},C=e=>{var o;null==(o=p(k))||o.setProps({size:e})},x=e=>{var o;null==(o=p(k))||o.setProps({disabled:e})},P=e=>{var o,l;e?null==(o=p(k))||o.delSchema("field2"):e||"field2"===D[1].field||null==(l=p(k))||l.addSchema({field:"field2",label:_("formDemo.select"),component:"Select",componentProps:{options:[{label:"option1",value:"1"},{label:"option2",value:"2"}]}},1)},g=e=>{var o,l;const t=null==(o=p(k))?void 0:o.getElFormRef();e?null==t||t.resetFields():null==(l=p(k))||l.setValues({field1:"field1",field2:"2",field3:"2",field4:["1","3"],field5:"2022-01-27",field6:"17:00"})},F=a(7),S=()=>{var e;null==(e=p(k))||e.setSchema([{field:"field2",path:"label",value:`${_("formDemo.select")} ${F.value}`},{field:"field2",path:"componentProps.options",value:[{label:"option-1",value:"1"},{label:"option-2",value:"2"},{label:"option-3",value:"3"}]}]),F.value++},$=()=>{var e,o;p(F)%2==0?null==(e=p(k))||e.addSchema({field:`field${p(F)}`,label:`${_("formDemo.input")}${p(F)}`,component:"Input"}):null==(o=p(k))||o.addSchema({field:`field${p(F)}`,label:`${_("formDemo.input")}${p(F)}`,component:"Input"},p(F)),F.value++},R=()=>{var e,o;const l=null==(e=p(k))?void 0:e.getElFormRef();null==(o=null==l?void 0:l.validate())||o.catch((()=>{}))},y=()=>{var e;const o=null==(e=p(k))?void 0:e.getElFormRef();null==o||o.resetFields()},E=async()=>{var e;const o=await c();o&&(null==(e=p(k))||e.setSchema([{field:"field2",path:"componentProps.options",value:o.data}]))};return(l,t)=>(m(),r(u,null,[s(p(o),{title:`RefForm ${p(_)("formDemo.operate")}`},{default:n((()=>[s(p(j),{onClick:t[0]||(t[0]=e=>h(150))},{default:n((()=>[d(f(p(_)("formDemo.change"))+" labelWidth",1)])),_:1}),s(p(j),{onClick:t[1]||(t[1]=e=>h("auto"))},{default:n((()=>[d(f(p(_)("formDemo.restore"))+" labelWidth",1)])),_:1}),s(p(j),{onClick:t[2]||(t[2]=e=>C("large"))},{default:n((()=>[d(f(p(_)("formDemo.change"))+" size",1)])),_:1}),s(p(j),{onClick:t[3]||(t[3]=e=>C("default"))},{default:n((()=>[d(f(p(_)("formDemo.restore"))+" size",1)])),_:1}),s(p(j),{onClick:t[4]||(t[4]=e=>x(!0))},{default:n((()=>[d(f(p(_)("formDemo.disabled")),1)])),_:1}),s(p(j),{onClick:t[5]||(t[5]=e=>x(!1))},{default:n((()=>[d(f(p(_)("formDemo.disablement")),1)])),_:1}),s(p(j),{onClick:t[6]||(t[6]=e=>P(!0))},{default:n((()=>[d(f(p(_)("formDemo.delete"))+" "+f(p(_)("formDemo.select")),1)])),_:1}),s(p(j),{onClick:t[7]||(t[7]=e=>P(!1))},{default:n((()=>[d(f(p(_)("formDemo.add"))+" "+f(p(_)("formDemo.select")),1)])),_:1}),s(p(j),{onClick:t[8]||(t[8]=e=>g(!1))},{default:n((()=>[d(f(p(_)("formDemo.setValue")),1)])),_:1}),s(p(j),{onClick:t[9]||(t[9]=e=>g(!0))},{default:n((()=>[d(f(p(_)("formDemo.resetValue")),1)])),_:1}),s(p(j),{onClick:S},{default:n((()=>[d(f(p(_)("formDemo.set"))+" "+f(p(_)("formDemo.select"))+" label ",1)])),_:1}),s(p(j),{onClick:$},{default:n((()=>[d(f(p(_)("formDemo.add"))+" "+f(p(_)("formDemo.subitem")),1)])),_:1}),s(p(j),{onClick:R},{default:n((()=>[d(f(p(_)("formDemo.formValidation")),1)])),_:1}),s(p(j),{onClick:y},{default:n((()=>[d(f(p(_)("formDemo.verifyReset")),1)])),_:1}),s(p(j),{onClick:E},{default:n((()=>[d(f(p(_)("searchDemo.dynamicOptions")),1)])),_:1})])),_:1},8,["title"]),s(p(o),{title:`RefForm ${p(_)("formDemo.example")}`},{default:n((()=>[s(p(e),{schema:D,ref_key:"formRef",ref:k},null,8,["schema"])])),_:1},8,["title"])],64))}});export{b as default};
