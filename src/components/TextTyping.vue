<script setup lang="ts" name="TextTyping">
    import { ref, onMounted } from 'vue'

    const props = defineProps<{
        content: string[]
        typeSpeed?: number
        deleteSpeed?: number
        waitTime?: number
    }>()

    const typeSpeed = props.typeSpeed ?? 100
    const deleteSpeed = props.deleteSpeed ?? 50
    const waitTime = props.waitTime ?? 2000

    const currentIndex = ref(0)
    const currentText = ref('')
    const deleting = ref(false)

    function sleep(ms: number) {
        return new Promise(resolve => setTimeout(resolve, ms))
    }

    async function startTyping() {
        while (true) {
            const fullText = props.content[currentIndex.value]
            if (!fullText) return

            if (!deleting.value) {
                if (currentText.value.length < fullText.length) {
                    currentText.value += fullText[currentText.value.length]
                    await sleep(typeSpeed)
                } else {
                    deleting.value = true
                    await sleep(waitTime)
                }
            } else {
                if (currentText.value.length > 0) {
                    currentText.value = currentText.value.slice(0, -1)
                    await sleep(deleteSpeed)
                } else {
                    deleting.value = false
                    currentIndex.value = (currentIndex.value + 1) % props.content.length
                }
            }
        }
    }

    onMounted(() => {
        startTyping()
    })
</script>

<template>
    <span>{{ currentText }}</span>
    <span class="cursor">|</span>
</template>

<style scoped>
    .cursor {
        animation: blink 1s infinite;
    }

    @keyframes blink {
        50% { opacity: 0; }
    }
</style>