<script setup lang="ts" name="Home">
    import CodeBlockFileLoader from '@/components/codeBlock/CodeBlockFileLoader.vue'
    import CodeBlockMarkdownLoader from '@/components/codeBlock/CodeBlockMarkdownLoader.vue'
    import TextTyping from '@/components/TextTyping.vue'
    
    const introductionTitleList = [
        ' to My Page', '! Glad You\'re Here', ' to My Blog', ' & Hello!'
    ]
</script>

<template>
    <main class="home-main">
        <section class="introduction">
            <h1>Welcome<TextTyping :content="introductionTitleList"/></h1>
            <p>I primarily program in Python and Java, with occasional coding in Ruby, C, and HTML/CSS/JavaScript.</p>
            <p>This is my personal test website where I practice and record my learning journey, including coding, language study, and anything else I explore.</p>
        </section>
        <!-- 待調整 -->
        <!-- <CodeBlockFileLoader lang="Python" src="/code/helloWorld.py" />
        <CodeBlockMarkdownLoader src="/markdown/helloWorld/HelloWorld.md" /> -->
    </main>
</template>

<style scoped>
    .home-main {
        flex: 1;
        padding: 20px;
    }

    .home-main .introduction p {
        font-size: 18px;
    }
</style>