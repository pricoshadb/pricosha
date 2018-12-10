<template lang="html">
  <div class="popup">
    
  </div>
</template>

<script>
export default {
  data() {
    return {
      visible: false
    }
  },
  directives: {
    'click-outside': {
      bind(el, binding, vNode) {
        if (typeof binding.value !== 'function') {
          return
        }
        const bubble = binding.modifiers.bubble
        const handler = (e) => {
          if (bubble || (! el.contains(e.target) && el !== e.target)) {
            binding.value(e)
          }
        }
        el.__vueClickOutside__ = handler
        document.addEventListener('click', handler)
      },
      unbind(el, binding) {
        document.removeEventListener('click', el.__vueClickOutside__)
        el.__vueClickOutside__ = null
      }
    }
  }
}
</script>

<style lang="css">
.popup {
  position: absolute;
}
</style>
