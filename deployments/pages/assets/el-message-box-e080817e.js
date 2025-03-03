import{C as e,x as n,ad as o,a6 as t,d as a,L as s,co as l,cp as r,v as i,r as c,q as u,cq as d,z as p,ah as f,aG as m,_ as v,H as g,o as y,h,w as b,K as C,g as E,e as x,n as B,X as w,aj as k,c as M,ai as T,y as I,t as S,J as z,O as R,B as _,aT as L,i as A,av as V,ax as j,be as P,cr as O,aV as $,$ as H,aM as q,aL as K,bq as D}from"./index-c922549f.js";import{E as U}from"./el-button-3322aa8d.js";import{E as F}from"./el-input-5992562e.js";import{E as G,u as J,b as W,a as X}from"./el-overlay-51fc3bc1.js";import{o as Z}from"./aria-ecee1d93.js";import{E as N}from"./focus-trap-8b9664b6.js";import{i as Q}from"./validator-ea5284a6.js";import{u as Y}from"./index-d069b56e.js";const ee="_trap-focus-children",ne=[],oe=e=>{if(0===ne.length)return;const n=ne[ne.length-1][ee];if(n.length>0&&e.code===t.tab){if(1===n.length)return e.preventDefault(),void(document.activeElement!==n[0]&&n[0].focus());const o=e.shiftKey,t=e.target===n[0],a=e.target===n[n.length-1];t&&o&&(e.preventDefault(),n[n.length-1].focus()),a&&!o&&(e.preventDefault(),n[0].focus())}},te=a({name:"ElMessageBox",directives:{TrapFocus:{beforeMount(e){e[ee]=Z(e),ne.push(e),ne.length<=1&&document.addEventListener("keydown",oe)},updated(e){o((()=>{e[ee]=Z(e)}))},unmounted(){ne.shift(),0===ne.length&&document.removeEventListener("keydown",oe)}}},components:{ElButton:U,ElFocusTrap:N,ElInput:F,ElOverlay:G,ElIcon:s,...l},inheritAttrs:!1,props:{buttonSize:{type:String,validator:Q},modal:{type:Boolean,default:!0},lockScroll:{type:Boolean,default:!0},showClose:{type:Boolean,default:!0},closeOnClickModal:{type:Boolean,default:!0},closeOnPressEscape:{type:Boolean,default:!0},closeOnHashChange:{type:Boolean,default:!0},center:Boolean,draggable:Boolean,roundButton:{default:!1,type:Boolean},container:{type:String,default:"body"},boxType:{type:String,default:""}},emits:["vanish","action"],setup(t,{emit:a}){const{locale:s,zIndex:l,ns:v,size:g}=r("message-box",i((()=>t.buttonSize))),{t:y}=s,{nextZIndex:h}=l,b=c(!1),C=u({autofocus:!0,beforeClose:null,callback:null,cancelButtonText:"",cancelButtonClass:"",confirmButtonText:"",confirmButtonClass:"",customClass:"",customStyle:{},dangerouslyUseHTMLString:!1,distinguishCancelAndClose:!1,icon:"",inputPattern:null,inputPlaceholder:"",inputType:"text",inputValue:null,inputValidator:null,inputErrorMessage:"",message:null,modalFade:!0,modalClass:"",showCancelButton:!1,showConfirmButton:!0,type:"",title:void 0,showInput:!1,action:"",confirmButtonLoading:!1,cancelButtonLoading:!1,confirmButtonDisabled:!1,editorErrorMessage:"",validateError:!1,zIndex:h()}),E=i((()=>{const e=C.type;return{[v.bm("icon",e)]:e&&d[e]}})),x=Y(),B=Y(),w=i((()=>C.icon||d[C.type]||"")),k=i((()=>!!C.message)),M=c(),T=c(),I=c(),S=c(),z=c(),R=i((()=>C.confirmButtonClass));e((()=>C.inputValue),(async e=>{await o(),"prompt"===t.boxType&&null!==e&&P()}),{immediate:!0}),e((()=>b.value),(e=>{var n,a;e&&("prompt"!==t.boxType&&(C.autofocus?I.value=null!=(a=null==(n=z.value)?void 0:n.$el)?a:M.value:I.value=M.value),C.zIndex=h()),"prompt"===t.boxType&&(e?o().then((()=>{var e;S.value&&S.value.$el&&(C.autofocus?I.value=null!=(e=O())?e:M.value:I.value=M.value)})):(C.editorErrorMessage="",C.validateError=!1))}));const _=i((()=>t.draggable));function L(){b.value&&(b.value=!1,o((()=>{C.action&&a("action",C.action)})))}J(M,T,_),p((async()=>{await o(),t.closeOnHashChange&&window.addEventListener("hashchange",L)})),f((()=>{t.closeOnHashChange&&window.removeEventListener("hashchange",L)}));const A=()=>{t.closeOnClickModal&&j(C.distinguishCancelAndClose?"close":"cancel")},V=X(A),j=e=>{var n;("prompt"!==t.boxType||"confirm"!==e||P())&&(C.action=e,C.beforeClose?null==(n=C.beforeClose)||n.call(C,e,C,L):L())},P=()=>{if("prompt"===t.boxType){const e=C.inputPattern;if(e&&!e.test(C.inputValue||""))return C.editorErrorMessage=C.inputErrorMessage||y("el.messagebox.error"),C.validateError=!0,!1;const n=C.inputValidator;if("function"==typeof n){const e=n(C.inputValue);if(!1===e)return C.editorErrorMessage=C.inputErrorMessage||y("el.messagebox.error"),C.validateError=!0,!1;if("string"==typeof e)return C.editorErrorMessage=e,C.validateError=!0,!1}}return C.editorErrorMessage="",C.validateError=!1,!0},O=()=>{const e=S.value.$refs;return e.input||e.textarea},$=()=>{j("close")};return t.lockScroll&&W(b),((o,t)=>{let a;e((()=>o.value),(e=>{var o,s;e?(a=document.activeElement,n(t)&&(null==(s=(o=t.value).focus)||s.call(o))):a.focus()}))})(b),{...m(C),ns:v,overlayEvent:V,visible:b,hasMessage:k,typeClass:E,contentId:x,inputId:B,btnSize:g,iconComponent:w,confirmButtonClasses:R,rootRef:M,focusStartRef:I,headerRef:T,inputRef:S,confirmRef:z,doClose:L,handleClose:$,onCloseRequested:()=>{t.closeOnPressEscape&&$()},handleWrapperClick:A,handleInputEnter:e=>{if("textarea"!==C.inputType)return e.preventDefault(),j("confirm")},handleAction:j,t:y}}}),ae=["aria-label","aria-describedby"],se=["aria-label"],le=["id"];var re=v(te,[["render",function(e,n,o,t,a,s){const l=g("el-icon"),r=g("close"),i=g("el-input"),c=g("el-button"),u=g("el-focus-trap"),d=g("el-overlay");return y(),h(A,{name:"fade-in-linear",onAfterLeave:n[11]||(n[11]=n=>e.$emit("vanish")),persisted:""},{default:b((()=>[C(E(d,{"z-index":e.zIndex,"overlay-class":[e.ns.is("message-box"),e.modalClass],mask:e.modal},{default:b((()=>[x("div",{role:"dialog","aria-label":e.title,"aria-modal":"true","aria-describedby":e.showInput?void 0:e.contentId,class:B(`${e.ns.namespace.value}-overlay-message-box`),onClick:n[8]||(n[8]=(...n)=>e.overlayEvent.onClick&&e.overlayEvent.onClick(...n)),onMousedown:n[9]||(n[9]=(...n)=>e.overlayEvent.onMousedown&&e.overlayEvent.onMousedown(...n)),onMouseup:n[10]||(n[10]=(...n)=>e.overlayEvent.onMouseup&&e.overlayEvent.onMouseup(...n))},[E(u,{loop:"",trapped:e.visible,"focus-trap-el":e.rootRef,"focus-start-el":e.focusStartRef,onReleaseRequested:e.onCloseRequested},{default:b((()=>[x("div",{ref:"rootRef",class:B([e.ns.b(),e.customClass,e.ns.is("draggable",e.draggable),{[e.ns.m("center")]:e.center}]),style:w(e.customStyle),tabindex:"-1",onClick:n[7]||(n[7]=k((()=>{}),["stop"]))},[null!==e.title&&void 0!==e.title?(y(),M("div",{key:0,ref:"headerRef",class:B(e.ns.e("header"))},[x("div",{class:B(e.ns.e("title"))},[e.iconComponent&&e.center?(y(),h(l,{key:0,class:B([e.ns.e("status"),e.typeClass])},{default:b((()=>[(y(),h(T(e.iconComponent)))])),_:1},8,["class"])):I("v-if",!0),x("span",null,S(e.title),1)],2),e.showClose?(y(),M("button",{key:0,type:"button",class:B(e.ns.e("headerbtn")),"aria-label":e.t("el.messagebox.close"),onClick:n[0]||(n[0]=n=>e.handleAction(e.distinguishCancelAndClose?"close":"cancel")),onKeydown:n[1]||(n[1]=z(k((n=>e.handleAction(e.distinguishCancelAndClose?"close":"cancel")),["prevent"]),["enter"]))},[E(l,{class:B(e.ns.e("close"))},{default:b((()=>[E(r)])),_:1},8,["class"])],42,se)):I("v-if",!0)],2)):I("v-if",!0),x("div",{id:e.contentId,class:B(e.ns.e("content"))},[x("div",{class:B(e.ns.e("container"))},[e.iconComponent&&!e.center&&e.hasMessage?(y(),h(l,{key:0,class:B([e.ns.e("status"),e.typeClass])},{default:b((()=>[(y(),h(T(e.iconComponent)))])),_:1},8,["class"])):I("v-if",!0),e.hasMessage?(y(),M("div",{key:1,class:B(e.ns.e("message"))},[R(e.$slots,"default",{},(()=>[e.dangerouslyUseHTMLString?(y(),h(T(e.showInput?"label":"p"),{key:1,for:e.showInput?e.inputId:void 0,innerHTML:e.message},null,8,["for","innerHTML"])):(y(),h(T(e.showInput?"label":"p"),{key:0,for:e.showInput?e.inputId:void 0},{default:b((()=>[_(S(e.dangerouslyUseHTMLString?"":e.message),1)])),_:1},8,["for"]))]))],2)):I("v-if",!0)],2),C(x("div",{class:B(e.ns.e("input"))},[E(i,{id:e.inputId,ref:"inputRef",modelValue:e.inputValue,"onUpdate:modelValue":n[2]||(n[2]=n=>e.inputValue=n),type:e.inputType,placeholder:e.inputPlaceholder,"aria-invalid":e.validateError,class:B({invalid:e.validateError}),onKeydown:z(e.handleInputEnter,["enter"])},null,8,["id","modelValue","type","placeholder","aria-invalid","class","onKeydown"]),x("div",{class:B(e.ns.e("errormsg")),style:w({visibility:e.editorErrorMessage?"visible":"hidden"})},S(e.editorErrorMessage),7)],2),[[L,e.showInput]])],10,le),x("div",{class:B(e.ns.e("btns"))},[e.showCancelButton?(y(),h(c,{key:0,loading:e.cancelButtonLoading,class:B([e.cancelButtonClass]),round:e.roundButton,size:e.btnSize,onClick:n[3]||(n[3]=n=>e.handleAction("cancel")),onKeydown:n[4]||(n[4]=z(k((n=>e.handleAction("cancel")),["prevent"]),["enter"]))},{default:b((()=>[_(S(e.cancelButtonText||e.t("el.messagebox.cancel")),1)])),_:1},8,["loading","class","round","size"])):I("v-if",!0),C(E(c,{ref:"confirmRef",type:"primary",loading:e.confirmButtonLoading,class:B([e.confirmButtonClasses]),round:e.roundButton,disabled:e.confirmButtonDisabled,size:e.btnSize,onClick:n[5]||(n[5]=n=>e.handleAction("confirm")),onKeydown:n[6]||(n[6]=z(k((n=>e.handleAction("confirm")),["prevent"]),["enter"]))},{default:b((()=>[_(S(e.confirmButtonText||e.t("el.messagebox.confirm")),1)])),_:1},8,["loading","class","round","disabled","size"]),[[L,e.showConfirmButton]])],2)],6)])),_:3},8,["trapped","focus-trap-el","focus-start-el","onReleaseRequested"])],42,ae)])),_:3},8,["z-index","overlay-class","mask"]),[[L,e.visible]])])),_:3})}],["__file","/home/runner/work/element-plus/element-plus/packages/components/message-box/src/index.vue"]]);const ie=new Map,ce=(e,n,o=null)=>{const t=E(re,e,K(e.message)||P(e.message)?{default:K(e.message)?e.message:()=>e.message}:null);return t.appContext=o,O(t,n),(e=>{let n=document.body;return e.appendTo&&(j(e.appendTo)&&(n=document.querySelector(e.appendTo)),D(e.appendTo)&&(n=e.appendTo),D(n)||(n=document.body)),n})(e).appendChild(n.firstElementChild),t.component},ue=(e,n)=>{const o=document.createElement("div");e.onVanish=()=>{O(null,o),ie.delete(a)},e.onAction=n=>{const o=ie.get(a);let s;s=e.showInput?{value:a.inputValue,action:n}:n,e.callback?e.callback(s,t.proxy):"cancel"===n||"close"===n?e.distinguishCancelAndClose&&"cancel"!==n?o.reject("close"):o.reject("cancel"):o.resolve(s)};const t=ce(e,o,n),a=t.proxy;for(const s in e)$(e,s)&&!$(a.$props,s)&&(a[s]=e[s]);return a.visible=!0,a};function de(e,n=null){if(!V)return Promise.reject();let o;return j(e)||P(e)?e={message:e}:o=e.callback,new Promise(((t,a)=>{const s=ue(e,null!=n?n:de._context);ie.set(s,{options:e,callback:o,resolve:t,reject:a})}))}const pe={alert:{closeOnPressEscape:!1,closeOnClickModal:!1},confirm:{showCancelButton:!0},prompt:{showCancelButton:!0,showInput:!0}};["alert","confirm","prompt"].forEach((e=>{de[e]=function(e){return(n,o,t,a)=>{let s="";return H(o)?(t=o,s=""):s=q(o)?"":o,de(Object.assign({title:s,message:n,type:"",...pe[e]},t,{boxType:e}),a)}}(e)})),de.close=()=>{ie.forEach(((e,n)=>{n.doClose()})),ie.clear()},de._context=null;const fe=de;fe.install=e=>{fe._context=e._context,e.config.globalProperties.$msgbox=fe,e.config.globalProperties.$messageBox=fe,e.config.globalProperties.$alert=fe.alert,e.config.globalProperties.$confirm=fe.confirm,e.config.globalProperties.$prompt=fe.prompt};const me=fe;export{me as E};
