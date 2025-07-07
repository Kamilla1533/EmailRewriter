import json

input_filepath = 'fixed_list_data.json'
output_filepath = 'fixed_list_data_1.json'


try:
    with open(input_filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    fixed_content = content.replace("NAG", "Non-Aggressive")
    fixed_content_1 = fixed_content.replace("CAG", "Covertly-Aggressive")
    fixed_content_2 = fixed_content_1.replace("OAG", "Overtly-Aggressive")

    data = json.loads(fixed_content_2)

    with open(output_filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Файл успешно исправлен и сохранен в '{output_filepath}'")

except FileNotFoundError:
    print(f"Ошибка: Файл '{input_filepath}' не найден")
except json.JSONDecodeError as e:
    print(f"Ошибка: Не удалось декодировать JSON даже после попытки исправления")
    print(f"Проблема, возможно, сложнее, чем просто отсутствующие запятые: {e}")

except Exception as e:
    print(f"Произошла ошибка: {e}")