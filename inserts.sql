INSERT INTO public.products(title, price) VALUES('azeite', 2.99);
INSERT INTO public.products(title, price) VALUES('cerveja', 0.99);
INSERT INTO public.products(title, price) VALUES('morango', 2.99);
INSERT INTO public.products(title, price) VALUES('pão', 0.08);
INSERT INTO public.products(title, price) VALUES('cafe', 1.99);
INSERT INTO public.products(title, price) VALUES('chocolate', 2.99);
INSERT INTO public.products(title, price) VALUES('vinho', 4.99);

INSERT INTO public.users (username, email, password_hash) VALUES('user', 'user@email.com', '1Password');

INSERT INTO public.carts (user_id, added_on) VALUES(1, now());

INSERT INTO public.cart_item (cart_id, product_id) VALUES(1, 1);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(1, 2);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(1, 3);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(1, 4);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(1, 5);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(1, 6);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(1, 7);

INSERT INTO public.vouchers (code, user_id, discount, added_on) VALUES('teste10', 1, 10, now());
INSERT INTO public.vouchers (code, user_id, discount, added_on) VALUES('voucher10', 1, 10, now());

INSERT INTO public.carts (user_id, voucher_id, added_on) VALUES(1, 1, now());

INSERT INTO public.cart_item (cart_id, product_id) VALUES(2, 1);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(2, 2);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(2, 3);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(2, 4);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(2, 5);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(2, 6);
INSERT INTO public.cart_item (cart_id, product_id) VALUES(2, 7);


