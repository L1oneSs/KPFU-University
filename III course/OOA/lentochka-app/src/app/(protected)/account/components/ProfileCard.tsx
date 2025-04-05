"use client"
import React, { ChangeEvent, useState, useEffect } from 'react';
import { useCurrentUser } from '@/hooks/useCurrentUser';
import { Button } from "@/components/ui/button"
import WishlistCard from '@/components/WishlistCard';
import { getStorage, ref, uploadBytesResumable, getDownloadURL } from "firebase/storage";
import { app } from '@/config/firebase';
import { useMutation, useQuery } from '@tanstack/react-query';
import AccountService from '@/services/AccountService';
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { useForm } from 'react-hook-form';
import * as z from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { FaFileImage } from "react-icons/fa";
import { Tiptap } from '@/components/ui/tiptap';
import { WishListItemSchema } from '@/schemas';
import toast from 'react-hot-toast';
import productService from '@/services/newProductService';
import WishlistService from '@/services/WishlistService';
import { useRouter } from 'next/navigation';






const ProfileCard = () => {
	const router = useRouter()
	const user = useCurrentUser();
	const [isEditing, setIsEditing] = useState<boolean>(false);
	const [editedName, setEditedName] = useState<string>(user?.name || '');
	const [editedNickname, setEditedNickname] = useState<string>(user?.nickname || '');
	const [editedDescription, setEditedDescription] = useState<string>(user?.description || '');

	const [media, setMedia] = useState<string>(user?.image || '');
	const [file, setFile] = useState<Blob | Uint8Array | ArrayBuffer>();
	const [disabledFromMedia, setDisabledFromMedia] = useState<boolean>(false);

	const [wishlistModalOpen, setWishlistModalOpen] = useState<boolean>(false)
	console.log(user)
	//const [editedDescription, setEditedDescription] = useState<string>('');

	interface iChange {
		image: string
		description: string
	}

	interface iChangeWishlist {
		image: string
		description: string
		name: string
		link: string
		hashtag: string
	}

	const mutation = useMutation({
		mutationKey: ["updateaccountdata"],
		mutationFn: (value: iChange) => AccountService.updatefriend(value),
	})

	const mutationWishlist = useMutation({
		mutationKey: ['new-post'],
		mutationFn: (values: z.infer<typeof WishListItemSchema>) => WishlistService.create(values),
		onSuccess: (data: any) => {
			toast.success('Вишлист успешно создан!')
			form.reset();
			router.push('/account')
		},
		onError: (error: any) => {
			console.log(error.message);
			toast.error(error.response.data.error);
		}
	});

	// const {data: userData, isSuccess} = useQuery({ 
	//       queryKey: ['user'],
	//       queryFn: () => AccountService.getUser(),
	//       select: ({data}) => data
	//   })

	const { data: wishlistData, isSuccess: isWishlistSuccess } = useQuery({
		queryKey: ['wishlist'],
		queryFn: () => WishlistService.getWishlists(),
		select: ({ data }) => data
	})

	console.log(wishlistData)

	useEffect(() => {
		const storage = getStorage(app);
		const upload = () => {
			if (file) {

				const name = new Date().getTime().toString();
				const storageRef = ref(storage, name);

				const uploadTask = uploadBytesResumable(storageRef, file);

				uploadTask.on(
					"state_changed",
					(snapshot) => {
						const progress =
							(snapshot.bytesTransferred / snapshot.totalBytes) * 100;
						console.log("Upload is " + progress + "% done");
						switch (snapshot.state) {
							case "paused":
								console.log("Upload is paused");
								break;
							case "running":
								console.log("Upload is running");
								break;
						}
					},
					(error) => { console.log(error.message) },
					() => {
						getDownloadURL(uploadTask.snapshot.ref).then((downloadURL) => {
							setMedia(downloadURL);
							setDisabledFromMedia(true);
							console.log('File available at', downloadURL);
						});
					}
				);
			}
		};

		file && upload();
	}, [file]);

	const handleEditClick = () => {
		setIsEditing(true);
	};

	const handleOpenWishlistClick = () => {
		setWishlistModalOpen(true)
	}

	const handleSaveClick = (media: string, editedDescription: string) => {
		// Отправка данных о профиле на сервер
		console.log(editedDescription)
		const obj: iChange = { image: media, description: editedDescription }
		mutation.mutate(obj)
		setIsEditing(false);
	};

	/*
	const handleNameChange = (event: ChangeEvent<HTMLInputElement>) => {
	  setEditedName(event.target.value);
	};
  
	const handleNicknameChange = (event: ChangeEvent<HTMLInputElement>) => {
	  setEditedNickname(event.target.value);
	};
	*/
	const handleDescriptionChange = (event: ChangeEvent<HTMLTextAreaElement>) => {
		console.log(event.target.value)
		setEditedDescription(event.target.value);
	};

	const slugify = (str: string) => str.toLowerCase().trim().replace(/\W_/g, "").replace(/\s/g, "-").replace(/^-+|-+$/g, "").replace(/а/g, "a").replace(/б/g, "b").replace(/в/g, "v").replace(/г/g, "g").replace(/д/g, "d").replace(/е/g, "e").replace(/ё/g, "yo").replace(/ж/g, "zh").replace(/з/g, "z").replace(/и/g, "i").replace(/й/g, "y").replace(/к/g, "k").replace(/л/g, "l").replace(/м/g, "m").replace(/н/g, "n").replace(/о/g, "o").replace(/п/g, "p").replace(/р/g, "r").replace(/с/g, "s").replace(/т/g, "t").replace(/у/g, "u").replace(/ф/g, "f").replace(/х/g, "kh").replace(/ц/g, "ts").replace(/ч/g, "ch").replace(/ш/g, "sh").replace(/щ/g, "shch").replace(/ъ/g, "").replace(/ы/g, "y").replace(/ь/g, "").replace(/э/g, "e").replace(/ю/g, "yu").replace(/я/g, "ya").slice(0, 30);

	const form = useForm<z.infer<typeof WishListItemSchema>>({
		resolver: zodResolver(WishListItemSchema)
	});

	const onSubmit = (values: z.infer<typeof WishListItemSchema>) => {
		console.log(media);

		const updatedValues = {
			img: media,
			...values
		};
		console.log('image mutation', updatedValues.img);
		mutationWishlist.mutate(
			updatedValues
		);
	};

	return (
		<div className="flex flex-col items-center justify-start h-full gap-y-20 bg-repeat bg-contain" style={{ backgroundImage: 'url("back2.jpg")', backgroundSize: 'auto' }}>
			<div className="flex items-center justify-center">
				<div className="md:flex items-center justify-center bg-white rounded-xl shadow-md p-4 mt-4">
					<div className="md:flex-shrink-0 relative">
						<img
							className="h-48 w-48 object-cover rounded-full mx-auto mt-6 md:mt-0 cursor-pointer transition-opacity duration-300 ease-in-out hover:opacity-80"
							src={media || "/avatar.png"}
							alt="Avatar"
						/>
						{isEditing && (
							<label
								htmlFor="avatar-upload"
								className="absolute h-48 w-48 inset-0 flex justify-center items-center bg-black bg-opacity-40 text-white text-3xl rounded-full cursor-pointer transition-opacity duration-300 ease-in-out hover:opacity-100"
							>
								<input
									id="avatar-upload"
									type="file"
									accept="image/*"
									onChange={(event) => {
										if (event.target.files && event.target.files.length > 0) {
											setFile(event.target.files[0]);
										}
									}}
									className="hidden"
								/>
								+
							</label>
						)}
					</div>
					<div className="p-8 w-full">
						{/* {isEditing ? (
              <div className="flex flex-row gap-x-2">
                <input
                  type="text"
                  value={editedName}
                  onChange={(e) => handleNameChange(e)}
                  className="mb-4 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:ring-blue-200"
                />
                <input
                  type="text"
                  value={editedNickname}
                  onChange={(e) => handleNicknameChange(e)}
                  className="mb-4 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:ring-blue-200"
                />
              </div>
            ) : ()} */}
						<div>
							<h2 className="text-2xl font-bold mb-2">{editedName}</h2>
							<p className="text-gray-500 mb-4">{editedNickname}</p>
						</div>
						{isEditing ? (
							<textarea
								value={editedDescription}
								onChange={(e) => handleDescriptionChange(e)}
								maxLength={50}
								className="mb-4 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:ring-blue-200 resize-none"
							/>
						) : (
							//<p className="text-gray-700 mb-4">{user?.description || "Расскажите о себе"}</p>
							<p className="text-gray-700 mb-4 max-w-40 overflow-x-auto">{editedDescription.length == 0 ? "Расскажите о себе" : editedDescription}</p>
						)}
						<div className="flex">
							{isEditing ? (
								<Button
									onClick={() => handleSaveClick(media, editedDescription)}
									className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2"
								>
									Сохранить
								</Button>
							) : (
								<Button
									onClick={handleEditClick}
									className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2"
								>
									Редактировать
								</Button>
							)}
						</div>
					</div>
				</div>
			</div>
			{wishlistModalOpen ? (
				<Button
					onClick={() => setWishlistModalOpen(false)}
					className="bg-blue-500 hover:bg-blue-700 text-white text-xl font-bold py-6 px-6 rounded mr-2"
				>
					Отменить
				</Button>
			) : (
				<Button
					onClick={handleOpenWishlistClick}
					className="bg-blue-500 hover:bg-blue-700 text-white text-xl font-bold py-6 px-6 rounded mr-2"
				>
					Создать вишлист
				</Button>
			)}

			{wishlistModalOpen && (
				<Card className='w-[1200px] xl:w-[1024px] lg:w-[767px] md:w-[650px] sm:w-[300px] shadow-md'>
					<CardHeader>
						<CardTitle>
							<p className='text-2xl font-semibold text-center md:text-lg'>
								🔑 Вишлист
							</p>
						</CardTitle>
					</CardHeader>
					<CardContent>
						<Form {...form}>
							<form
								className='grid gap-y-6'
								onSubmit={form.handleSubmit(onSubmit)}
							>
								<FormField
									control={form.control}
									name='name'
									render={({ field }) => (
										<FormItem>
											<FormControl>
												<Input
													{...field}
													placeholder='Заголовок'
													disabled={mutation.isPending}
												/>
											</FormControl>
											<FormMessage />
										</FormItem>
									)}
								/>
								<FormField
									control={form.control}
									name='link'
									render={({ field }) => (
										<FormItem>
											<FormControl>
												<Input
													{...field}
													placeholder='Ссылка'
													type='url'
													disabled={mutation.isPending}
												/>
											</FormControl>
											<FormMessage />
										</FormItem>
									)}
								/>
								<FormField
									control={form.control}
									name='hashtag'
									render={({ field }) => (
										<FormItem>
											<Select
												disabled={mutation.isPending}
												onValueChange={field.onChange}
											>
												<FormControl>
													<SelectTrigger>
														<SelectValue
															placeholder='Выберите категорию'

														/>
													</SelectTrigger>
												</FormControl>
												<SelectContent>
													<SelectItem value='electronics'>
														Электроника
													</SelectItem>
													<SelectItem value='jewelry'>
														Ювелирное украшение
													</SelectItem>
												</SelectContent>
											</Select>
											<FormMessage />
										</FormItem>
									)}
								/>
								<FormField
									control={form.control}
									name='image'
									render={({ field }) => (
										<FormItem>
											<FormLabel
												className='grid justify-center items-center bg-indigo-900 w-[32px] h-[32px] rounded-[50%]'
												htmlFor="image"
											>
												<FaFileImage width={16} height={16} color='#F5EFEF' />
											</FormLabel>
											<FormControl>
												<Input
													{...field}
													type="file"
													id='image'
													disabled={mutation.isPending}
													onChange={(event) => {
														if (event.target.files && event.target.files.length > 0) {
															setFile(event.target.files[0]);
														}
													}}
													style={{ display: 'none' }}
												/>
											</FormControl>
											<FormMessage />
										</FormItem>
									)}
								/>

								<FormField
									control={form.control}
									name='description'
									render={({ field }) => (
										<FormItem>
											<FormControl>
												<Tiptap
													onChange={field.onChange}
												/>
											</FormControl>
											<FormMessage />
										</FormItem>
									)}
								/>
								<Button
									type='submit'
									className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-4 px-4 rounded mr-2'
									disabled={mutation.isPending && disabledFromMedia}
								>
									Создать новую запись
								</Button>
							</form>
						</Form>
					</CardContent>
				</Card>
			)}
			<div className="text-3xl font-bold bg-white rounded-xl shadow-md p-4">Ваши вишлисты</div>
			{isWishlistSuccess && (<WishlistCard products={wishlistData}></WishlistCard>)
			}
		</div>
	);
};

export default ProfileCard;
