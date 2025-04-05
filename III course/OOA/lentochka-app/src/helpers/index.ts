export const truncateText = (text: string, limit: number): string => {
	const words = text.split(" ");
	if (words.length > limit) {
		return words.slice(0, limit).join(" ") + "..";
	}
	return text;
};

export const formatTime = (date: Date) => {
	const dateObj = new Date(date);
	const month = ['Января', 'Февраля', 'Марта', 'Апреля', 'Мая', 'Июня', 'Июля', 'Августа', 'Сентября', 'Октября', 'Ноября', 'Декабря',]
	let tmp;
	return ((tmp = dateObj.getDate()))
		+ ' ' + (tmp = month[dateObj.getMonth()])
		+ ' ' + ((tmp = (dateObj.getFullYear())) < 10 ? '0' + tmp : tmp);
}