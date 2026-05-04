<script setup lang="ts" name="IntroductionTyping">
    import { useIntroductionTyping } from '@/hooks/about/useIntroductionTyping'
    import { watch } from 'vue'


    const { displayLines, startTyping } = useIntroductionTyping()
    const props = defineProps<{
        typingStart: boolean
        isMobile: boolean
    }>()

    // 監聽 typingStart 才開始打字
    watch(() => props.typingStart, (val) => {
        if (val) startTyping(props.isMobile)
    })
    
</script>

<template>
    <div v-for="(line, i) in displayLines" :key="i">
        <span v-if="line !== '\n'">{{ line }}</span>
        <span v-else><br /></span>
        <span v-if="i === displayLines.length - 1" class="cursor">|</span>
    </div>
</template>

<style scoped>
    .cursor {
        animation: blink 1s infinite;
    }

    @keyframes blink {
        50% {
            opacity: 0;
        }
    }
</style>