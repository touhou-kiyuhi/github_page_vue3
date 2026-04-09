<script setup lang="ts" name="HomeHeader">
    import catInBox from '@/assets/logo.svg'
    import { ref } from 'vue'
    import useMail from '@/hooks/useMail'
    
    
    const isMenuOpen = ref(false)
    const toggleMenu = () => {
        isMenuOpen.value = !isMenuOpen.value
    }

    const links = [
        { name: "Home", path: "/home", id: "home-link" },
        { name: "About", path: "/about", id: "about-link" }
    ]

    const { mailContact } = useMail()
</script>

<template>
    <header>
        <div class="logo" id="toggle-theme" style="cursor: pointer;">
            <img :src="catInBox" alt="Site Logo" title="窩是隻卯咪！！ 嗷嗷嗷！！">
        </div>
        <!-- "Hamburger menu" / "Bar icon" to toggle the navigation links -->
        <div class="mobile-menu" @click="toggleMenu">
            <a class="active"><i class="fa fa-bars"></i></a>
        </div>
        <nav id="header-links" :class="{ show: isMenuOpen }">
            <ul>
                <li v-for="link in links" :key="link.id">
                    <RouterLink :to="link.path" :id="link.id"> {{ link.name }} </RouterLink>
                </li>
                <li><a href="#contact" @click="mailContact">Contact</a></li>
            </ul>
        </nav>
    </header>
</template>

<style scoped>
    header {
        background-color: #333;
        color: white;
        padding: 10px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    header .logo img {
        width: 50px;
    }

    header nav ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        display: flex;
    }

    header nav ul li {
        margin-right: 20px;
    }

    header nav ul li a {
        color: white;
        text-decoration: none;
        font-weight: bold;
    }

    header .mobile-menu {
        display: none;
    }

    /* 響應式樣式 */
    @media (max-width: 500px) {
        /* Style the navigation menu */
        header {
            flex-direction: column;
            align-items: flex-start;
        }

        header nav ul {
            display: flex;
            flex-direction: column; /* 將項目改為垂直排列 */
        }

        /* Hide the links inside the navigation menu (except for logo/home) */
        header #header-links {
            display: none;
            flex-direction: column;
            width: 100%;
            background-color: #333;
        }

        /* 讓 .show 顯示出來 */
        header #header-links.show {
            display: flex;
        }

        /* Style the hamburger menu */
        header .mobile-menu {
            display: block;
            position: absolute;
            right: 0;
            margin-right: 15px;
        }

        /* Style navigation menu links */
        header a {
            padding: 14px 16px;
            font-size: 17px;
            display: block;
            text-align: center;
        }

        /* Add a grey background color on mouse-over */
        header a:hover {
            background-color: #ddd;
            color: black;
        }

        /* Style the active link (or home/logo) */
        .active {
            background-color: #333;
            color: white;
        }
    }
</style>