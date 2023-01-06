import pyautogui
from time import sleep

print(pyautogui.size())
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

absolute_coord_lun = 728, 495
absolute_coord_mar = 856, 495
absolute_coord_mer = 1029, 495
absolute_coord_gio = 1146, 495
absolute_coord_ven = 1324, 495
absolute_coord_sab = 1428, 495
absolute_coord_dom = 1599, 495

abs_coords = [absolute_coord_lun, absolute_coord_mar, absolute_coord_mer, absolute_coord_gio, absolute_coord_ven,
              absolute_coord_sab, absolute_coord_dom]

sleep(2)
prenota_btn_normale = (727, 558)
prenota_btn_abbassato = (727, 620)
prenota_pxl_color = (0, 123, 255)
red_alert_color = (248, 215, 218)
green_alter_color = (212, 237, 218)
alert_bar_coord = (1200, 573)
back_btn = (29, 118)
people_num_text_area_coords = (948, 396)
prenotazione_form_coords = (706, 553)


def click_twice_rapid(coord_tuple):
    for i in range(2):
        pyautogui.click(coord_tuple)
        sleep(0.5)


def get_pxl_color():
    sleep(1)
    mouse_pos = pyautogui.position()
    im = pyautogui.screenshot()
    print(im.getpixel(mouse_pos))


def type_n_persons(n):
    pyautogui.click(people_num_text_area_coords)
    pyautogui.press("backspace")
    pyautogui.write(n)


def main():
    sleep(1)
    type_n_persons("1")
    for idx, i in enumerate(abs_coords):
        click_twice_rapid(i)
        im = pyautogui.screenshot()
        pixel = im.getpixel(alert_bar_coord)

        while pixel == green_alter_color:
            pyautogui.click(prenota_btn_abbassato)
            pyautogui.click(prenota_btn_normale)  # click on prenota
            sleep(1)
            im1 = pyautogui.screenshot()
            pixel_booking_form = im1.getpixel(prenotazione_form_coords)
            pyautogui.click(back_btn)  # go back
            sleep(1)
            pyautogui.click(i)  # show alert bar again

            print(pixel_booking_form)
            if pixel_booking_form == (255, 255, 255):  # se mancano meno di 5 posti
                type_n_persons("5")
            else:
                type_n_persons("1")
            #  aggiorno la condizione
            print("taking screenshot")
            im = pyautogui.screenshot()
            pixel = im.getpixel(alert_bar_coord)
            print(pixel == green_alter_color)

    #     click_twice_rapid(prenota_btn)

main()
# get_pxl_color()