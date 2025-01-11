const mysql = require('mysql2/promise'); // استفاده از نسخه Promise

// ایجاد اتصال به دیتابیس
const connectionConfig = {
    host: 'kazbek.liara.cloud', // آدرس سرور دیتابیس
    user: 'root', // نام کاربری دیتابیس
    password: 'jcAetE0zOzd9grEdw5UFgwWK', // رمز عبور دیتابیس
    database: 'sso' // نام دیتابیس
};

const { getUsernameFromURL } = require('./scripts.js');

// تابع برای خواندن توکن از دیتابیس
async function getToken() {
    const connection = await mysql.createConnection(connectionConfig);
    try {
        const [results] = await connection.query('SELECT token FROM sso_sms LIMIT 1;');
        return results; // برگرداندن داده‌ها
    } catch (err) {
        console.error('Error executing query:', err.stack);
        throw err; // پرتاب خطا برای مدیریت در تابع فراخوانی
    } finally {
        await connection.end(); // بستن اتصال
    }
}

// تابع برای ذخیره شماره موبایل
async function save(phone) {
    const connection = await mysql.createConnection(connectionConfig);
    try {
        const username = getUsernameFromURL();
        const [results] = await connection.query('UPDATE sso_sms SET source = ? WHERE mobile = ?', [username, phone]);
        return results;
    } catch (err) {
        console.error('Error executing query:', err.stack);
        throw err; // پرتاب خطا برای مدیریت در تابع فراخوانی
    } finally {
        await connection.end(); // بستن اتصال
    }
}

var current_fs, next_fs, previous_fs;
var left, opacity, scale;
var animating;

function login() {
    const phoneInput = document.getElementById("phone"); // دریافت عنصر در اینجا
    const phone = phoneInput.value; // مقدار شماره تلفن
    const phonePattern = /^[0-9]{11}$/;

    if (phonePattern.test(phone)) {
        // فراخوانی API برای اعتبارسنجی شماره تلفن
        $.ajax({
            url: 'http://127.0.0.1:8080/api/create_mobile/', // آدرس API خود را اینجا قرار دهید
            type: 'POST',
            contentType: 'application/json', // مشخص کردن نوع محتوا به عنوان JSON
            data: JSON.stringify({ mobile: phone }), // ارسال داده‌ها به فرمت JSON
            success: function(response) {
                if (response) {
                    $(".next").off('click').on('click', function () { // استفاده از off و on برای جلوگیری از چندین بار ثبت رویداد
                        if (animating) return false;
                        animating = true;

                        document.getElementById('username2').innerText = 'نام کاربری: ' + phone;
                        current_fs = $(this).parent();
                        next_fs = $(this).parent().next();

                        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");

                        next_fs.show();
                        current_fs.animate({ opacity: 0 }, {
                            step: function (now, mx) {
                                scale = 1 - (1 - now) * 0.2;
                                left = (now * 50) + "%";
                                opacity = 1 - now;
                                current_fs.css({ 'transform': 'scale(' + scale + ')' });
                                next_fs.css({ 'left': left, 'opacity': opacity });
                            },
                            duration: 800,
                            complete: function () {
                                current_fs.hide();
                                animating = false;
                            },
                            easing: 'easeInOutBack'
                        });

                        // فراخوانی تابع save برای ذخیره اطلاعات
                        save(phone).then(() => {
                            console.log('اطلاعات با موفقیت ذخیره شد.');
                        }).catch(err => {
                            console.error('خطا در ذخیره اطلاعات:', err);
                        });
                    });
                } else {
                    alert('شماره تلفن معتبر نیست.');
                }
            },
            error: function(xhr) {
                if (xhr.status === 400) {
                    alert('خطا در اعتبارسنجی: ' + xhr.responseJSON.detail);
                } else {
                    alert('خطا در برقراری ارتباط با سرور.');
                }
            }
        });
    } else {
        alert('لطفاً یک شماره تلفن معتبر وارد کنید.');
    }
}

function goBack() {
    // پاک کردن ورودی کد
    document.getElementById('code').value = '';
    // بازگشت به فیلد قبلی
    $(".previous").click();
}

function verifyCode() {
    const codeInput = document.getElementById('code').value;
    // فراخوانی API برای تأیید کد
    $.ajax({
        url: 'http://127.0.0.1:8080/api/verify_code/', // آدرس API تأیید خود را اینجا قرار دهید
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ code: codeInput }), // ارسال داده‌ها به فرمت JSON
        success: function(response) {
            if (response.success) {
                alert('ورود موفقیت آمیز بود!');
                // هدایت به صفحه بعد
                window.location.href = 'nextPage.html'; // آدرس صفحه بعد خود را اینجا قرار دهید
            } else {
                alert('کد اشتباه است. لطفاً دوباره تلاش کنید.');
                // قفل کردن کاربر برای 3 دقیقه
                setTimeout(function() {
                    alert('شما نمی‌توانید دوباره تلاش کنید تا 3 دقیقه دیگر.');
                }, 180000); // 3 دقیقه
            }
        },
        error: function() {
            alert('خطا در برقراری ارتباط با سرور.');
        }
    });
}

// مثال استفاده از تابع getToken
async function exampleUsage() {
    try {
        const token = await getToken();
        console.log('توکن دریافتی:', token);
    } catch (error) {
        console.error('خطا در دریافت توکن:', error);
    }
}

// فراخوانی تابع مثال
login();
exampleUsage();