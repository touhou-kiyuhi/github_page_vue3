<script setup lang="ts" name="About">
    import ProfileCard from '@/components/ProfileCard.vue'
    import { ref, watch } from 'vue'
    import { useAboutPageMoveCard } from '@/hooks/about/useMoveCard'
    import IntroductionTyping from '@/components/IntroductionTyping.vue'


    const { moveCard, isMobile } = useAboutPageMoveCard()
    const IntroductionStartTyping = ref(false)
    const startTyping = () => {
        setTimeout(() => IntroductionStartTyping.value = true, 1000)
    }
    // desktop 
    watch(moveCard, (val) => {
        if (!isMobile && val) startTyping()
    })
    // mobile 
    if (isMobile) startTyping()
</script>

<template>
    <main id="about-main">
        <div id="introduction-animation">
            <div class="introduction-text-content">
                <IntroductionTyping 
                    :typingStart="IntroductionStartTyping"
                    :isMobile="isMobile"
                />
            </div>
            <div :class="['profile-card-content', { 'move-to-4': moveCard }]">
                <!-- Profile Card -->
                <ProfileCard />
            </div>
        </div>
        <!-- 待續 -->
        <!-- <div>
            <ProfileCard />
        </div> -->
    </main>
</template>

<style scoped>
    #about-main {
        display: flex;
        flex-direction: column; /* 讓 introduction-animation + 其他內容上下排列 */
        justify-items: center;
        align-items: center;
        gap: 40px;
    }

    #introduction-animation {
        display: grid; /* 改為 grid，取代 flex 撐開方式 */
        grid-template-columns: repeat(5, 1fr); /* 水平切成 5 等分 */
        justify-items: center; /* 讓每格內容水平置中 */
        align-items: center;   /* 垂直置中 */
        min-height: 100vh;
    }

    /* introduction text 不受邊界限制 */
    .introduction-text-content {
        /* grid-column: 1; 放第 1 格 */
        text-align: left;
        font-size: large;

        opacity: 1;                 /* 初始透明隱藏 */
        font-family: monospace;     /* 使用等寬字體，打字效果更自然 */
        white-space: normal;        /* 防止換行 */
        display: inline-block;      /* 使文字按行顯示 */
        visibility: visible;         /* 隱藏文字 */
        transition: opacity 1s ease; /* 當打字開始時才顯示 */

        /* 調整在打字動畫時，可跨越 column 並不會與 user card 重疊 */
        position: absolute;         /* 讓文字可以超出邊界 */
        left: 30%;                  /* 讓文字在第二格的中間顯示 */
        transform: translateX(-50%); /* 用此偏移讓文字居中並超出左右邊界 */
    }

    /* profile card 一開始在第 3 格 */
    .profile-card-content {
        grid-column: 3 / 4;
        max-width: 400px;
        width: 100%;

        /* 新增以下動畫設定 */
        transition: transform 1s ease;
        transform: translateX(0); /* 初始位置 */
    }

    /* profile card 移動到第 4 格 */
    .profile-card-content.move-to-4 {
        transform: translateX(100%);
    }

    @media (max-width: 1000px) {
        /* 中間內容區會自動撐開剩餘高度 */
        #introduction-animation {
            flex-direction: column-reverse; 
            display: flex;
            flex: 1; /* 撐開剩餘空間 */
            padding: 20px;
            justify-content: center; /* 水平置中整個內容區 */
            gap: 20px;
        }

        /* introduction text 位置固定，不用移動 */
        .introduction-text-content {
            /* 在第 3 格 */
            grid-column: 2 / 3;
            text-align: left;
            white-space: normal; /* 防止換行 */
            position: static;
            transform: none !important;
        }

        /* profile card 位置固定，不用移動 */
        .profile-card-content {
            position: static;
            transform: none !important;
            transition: none !important;
        }
    }
</style>