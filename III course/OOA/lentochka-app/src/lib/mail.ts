import nodemailer from 'nodemailer';

const domain = process.env.NEXT_PUBLIC_APP_URL;
const login = process.env.MAIL_LOGIN;
const password = process.env.MAIL_PASSWORD;


var transport = nodemailer.createTransport({
	host: "smtp.mail.ru",
	port: 465,
	auth: {
		user: login,
		pass: password
	}
});


export const sendTwoFactorTokenEmail = async (email: string, token: string) => {
	try {

		const mailOptions = {
			from: 'khasan07@list.ru',
			to: email,
			subject: '2ФА код',
			html: `<p>Ваш код 2ФА: ${token}<p>`
		}

		const mailresponse = await transport.sendMail(mailOptions);
		return mailresponse;

	} catch (error: any) {
		throw new Error(error.message);
	}
}


export const sendPasswordResetEmail = async (email: string, token: string) => {
	try {
		const resetLink = `${domain}/auth/new-password?token=${token}`;


		const mailOptions = {
			from: 'khasan07@list.ru',
			to: email,
			subject: 'Сбросить пароль',
			html: `<p>Нажмите <a href="${resetLink}">сюда</a>, чтобы сбросить пароль.<p>`
		};

		const mailresponse = await transport.sendMail(mailOptions);

		return mailresponse;

	} catch (error: any) {
		throw new Error(error.message);
	}
};


export const sendVerificationEmail = async (email: string, token: string) => {
	try {
		const confirmLink = `${domain}/auth/new-verification?token=${token}`;

		const mailOptions = {
			from: 'khasan07@list.ru',
			to: email,
			subject: 'Подтвердите свой адрес электронной почты',
			html: `<p>Нажмите <a href="${confirmLink}">сюда</a>, чтобы подтвердить свой email.<p>`
		};

		const mailresponse = await transport.sendMail(mailOptions);

		return mailresponse;

	} catch (error: any) {
		throw new Error(error.message);
	}
};
