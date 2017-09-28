free_proxy_list_lua = """
local ip_list = ""

function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(0.5))
  splash:evaljs("$(\\"select[name='proxylisttable_length']\\").val(\\"80\\");$(\\"select[name='proxylisttable_length']\\").trigger(\\"change\\")")
  while splash:evaljs("$(\\"#proxylisttable_next\\")[\\"0\\"].classList.contains(\\"disabled\\")")==false do
     ip_list = ip_list .. splash:evaljs("$(\\"#proxylisttable\\")[\\"0\\"].innerText")
     splash:evaljs("$(\\"#proxylisttable_next\\").trigger(\\"click\\")")
  end
  ip_list = ip_list .. splash:evaljs("$(\\"#proxylisttable\\")[\\"0\\"].innerText")
  
  return ip_list
end
"""

def free_proxy_list_lua_source():
    return free_proxy_list_lua
