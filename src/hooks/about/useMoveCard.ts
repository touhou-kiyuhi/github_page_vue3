import { ref, onMounted } from 'vue'

export function useAboutPageMoveCard() {
    const moveCard = ref(false)
    const isMobile = window.innerWidth <= 1000

    onMounted(() => {
        if (!isMobile) setTimeout(() => { moveCard.value = true }, 1500)
    })

    return { moveCard, isMobile }
}