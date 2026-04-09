<script setup lang="ts" name="HomeAside">
    import { computed } from 'vue'
    import { useRoute } from 'vue-router'
    import ProfileCard from '@/components/ProfileCard.vue'


    const route = useRoute()
    const isNotAbout = computed(() => route.path !== '/about')
    const links = [
        { name: "Home", path: "/home", id: "home-link" },
        { name: "Categories", path: "/categories", id: "categories-link" }
    ]
</script>

<template>
    <div v-if="isNotAbout" class="content-asides">
        <aside>
            <h3>Related Articles</h3>
            <ul>
                <li v-for="link in links" :key="link.id">
                    <RouterLink :to="link.path" :id="link.id"> {{ link.name }} </RouterLink>
                </li>
                <!-- 待設計 -->
                <!-- <li><a id="theBattleCatsPortfolio-link" href="#TheBattleCatsPortfolio">The Battle Cats</a></li> -->
                <!-- <li><a id="languagesStudy-link" href="#languagesStudy">Languages Study</a></li> -->
            </ul>
        </aside>
        <!-- Profile Card -->
        <aside>
            <ProfileCard/>
        </aside>
    </div>
</template>

<style scoped>
    /* Aside 區塊（桌面） */
    .content-asides {
        width: 250px;
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    aside {
        padding: 10px;
        /* light mode */
        background-color: #ddd;
    }

    aside a {
        /* light mode */
        color: #007acc;
    }

    aside a:hover {
        /* light mode */
        color: #005b99;
    }

    aside ul {
        list-style-type: none;
        padding: 0;
    }

    aside ul li {
        margin: 5px 0;
    }

    /* ========= 🔁 響應式調整（手機） ========= */
    @media (max-width: 610px) {
        .content-asides {
            width: 100%; /* 滿版 */
            order: -1;    /* 移到 main 上面 */
        }
    }
</style>