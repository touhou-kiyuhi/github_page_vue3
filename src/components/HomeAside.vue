<script setup lang="ts" name="HomeAside">
    import ProfileCard from '@/components/ProfileCard.vue'


    const sections = [
        {
            title: "Related Articles",
            links: [
                { name: "Home", label: "Home" },
                { name: "Categories", label: "Categories" }
            ]
        },
        {
            title: "Portfolio",
            links: [
                { name: "TheBattleCatsPortfolio", label: "The Battle Cats Portfolio" }
            ]
        },
        {
            title: "Utilities",
            links: [
                { name: "SudokuSolver", label: "Sudoku Solver" }
            ]
        },
        {
            title: "Demo Areas",
            links: [
                { name: "Demo", label: "Demo" }
            ]
        }
    ]
</script>

<template>
    <div class="content-asides">
        <aside>
            <div v-for="section in sections" :key="section.title">
                <h3>{{ section.title }}</h3>
                <ul>
                    <li v-for="link in section.links" :key="link.name">
                        <RouterLink :to="{ name: link.name }">
                            {{ link.label }}
                        </RouterLink>
                    </li>
                    <!-- 待設計 -->
                    <!-- <li><a id="theBattleCatsPortfolio-link" href="#TheBattleCatsPortfolio">The Battle Cats</a></li> -->
                    <!-- <li><a id="languagesStudy-link" href="#languagesStudy">Languages Study</a></li> -->
                </ul>
            </div>
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