from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
#from googletrans import Translator
from deep_translator import GoogleTranslator

#translator = Translator()

class FAQ(models.Model):
    question = models.TextField(null=True)
    answer = RichTextField()

    async def get_translation(self, lang='en', field='question'):
        cache_key = f'faq_{self.id}_{field}_{lang}'
        cached_translation = cache.get(cache_key)

        if cached_translation:
            return cached_translation
        text_to_translate = self.answer if field == 'answer' else self.question

        try:
            translation_result =GoogleTranslator(source='auto', target=lang).translate(text_to_translate)
            # Check the type of translation_result
            print(f"Translation Result: {translation_result}")
            
        except AttributeError:
            # Handle the case where translation_result is not a translation object
            print(f"Translation failed: Translation result has no 'text' attribute. Got: {translation_result}")
            return text_to_translate
        except Exception as e:
            print(f"Translation failed: {e}")
            return text_to_translate

        cache.set(cache_key, translation_result, timeout=3600)
        return translation_result

    def __str__(self):
        return self.question
