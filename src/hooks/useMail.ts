export default function () {
    const mailAddress = "dongfangjixuezhong@gmail.com"
    const mailSubject = "Email from Kiyuhi-Touhou Website"
    const mailBody = "Hello, I have something I'd like to ask you..."

    function mailContact() {
        const encodedSubject = encodeURIComponent(mailSubject)
        const encodedBody = encodeURIComponent(mailBody)

        window.location.href = `mailto:${mailAddress}?subject=${encodedSubject}&body=${encodedBody}`
    }

    return { mailContact }
}