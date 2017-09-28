kuaidaili_lua = """
function main(splash, args)
  splash:go(args.url)
  splash:wait(3.0)
  return splash:html()
end
"""

def kuaidaili_lua_source():
    return kuaidaili_lua
