<script setup lang="ts">
    defineProps<{
        visible: boolean
    }>()
</script>

<template>
	<!-- <Transition name="page" mode="out-in">
		<slot />
	</Transition> -->
    <transition name="fade">
        <div v-if="visible" class="overlay">
            <div class="spinner"></div>
        </div>
    </transition>
</template>

<style scoped>
    .overlay {
        position: fixed;
        inset: 0;
        background: rgba(128,128,128,0.3);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    }

    /* CSS Spinner（取代 GIF） */
    .spinner {
        width: 50px;
        height: 50px;
        border: 5px solid #ddd;
        border-top-color: #409eff;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }

    @keyframes spin {
        to { transform: rotate(360deg); }
    }

    /* 淡入淡出 */
    .fade-enter-active, .fade-leave-active {
        transition: opacity 0.2s;
    }
    .fade-enter-from, .fade-leave-to {
        opacity: 0;
    }
    /* .page-enter-from {
        opacity: 0;
        transform: translateY(20px);
    }

    .page-enter-active {
        transition: all 0.4s ease;
    }

    .page-enter-to {
        opacity: 1;
        transform: translateY(0);
    }

    .page-leave-from {
        opacity: 1;
        transform: translateY(0);
    }

    .page-leave-active {
        transition: all 0.3s ease;
    }

    .page-leave-to {
        opacity: 0;
        transform: translateY(-10px);
    } */
</style>