# Encoded By ALINUR RAHMAN
# https://github.com/AxR-99
import marshal, zlib, base64 
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))